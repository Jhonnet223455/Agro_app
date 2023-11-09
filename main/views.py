from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProductForm, FarmerForm
from django.contrib.auth.decorators import login_required
from .decorators import is_not_farmer, is_farmer
from .models import Agricultural_product, Farmer


def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    try:
        farmer = Farmer.objects.get(user=request.user)
        products_list = Agricultural_product.objects.filter(seller=farmer)
    except Farmer.DoesNotExist:
        farmer = None
        products_list = None

    return render(request, 'profile.html', {
        'products_list': products_list
    })

def unauthorized(request):
    return render(request, 'unauthorized_page.html')


@is_not_farmer
@login_required
def farmer_register(request):
    if request.method == 'GET':
        return render(request, 'farmer_register.html', {
            'form': FarmerForm
        })
    else:
        try:
            form = FarmerForm(request.POST)
            if form.is_valid():
                farmer = form.save(commit=False)
                farmer.user = request.user  # Asignar el usuario actual al campo 'user' del Farmer
                farmer.saldo = 0
                farmer.save()
                return redirect('profile')
        except ValueError:
            return render(request, 'farmer_register.html', {
                'form': FarmerForm,
                "error": "Invalid data"
            })


def products(request):
    products_list = Agricultural_product.objects.all()

    return render(request, 'products.html', {
        'products_list' : products_list
    })

@is_farmer
@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            new_product = form.save(commit=False)

            # Obtén el Farmer asociado al usuario autenticado
            farmer = Farmer.objects.get(user=request.user)

            new_product.seller = farmer
            new_product.save()

            return redirect('products')
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})

        

def product_detail(request, product_id):
    product = get_object_or_404(Agricultural_product, pk=product_id)
    return render(request, 'product_detail.html', {
        'product' : product,
    })


def product_delete(request, product_id):
    product = get_object_or_404(Agricultural_product, pk=product_id)
    if request.method == 'GET':
        if request.user == product.seller.user:
            product.delete()
            return redirect('profile')
    

@login_required
def product_edit(request, product_id):
    if request.method == 'GET':
        product = get_object_or_404(Agricultural_product, pk=product_id)
        if request.user == product.seller.user:
            form = ProductForm(instance=product)
            return render(request, 'product_edit.html', {
                'product' : product,
                'form' : form
            })
        else:
            return redirect('profile')
    
    else:
        try:
            product = get_object_or_404(Agricultural_product, pk=product_id)
            if request.user == product.seller.user:
                form = ProductForm(request.POST, instance=product)
                form.save()
                return redirect('profile')
        except ValueError:
            return render(request, 'product_edit.html', {
            'product' : product,
            'form' : form,
            'error' : 'Error Al Actualizar Producto'
            })




def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('products')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": "User already exists"
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": "Password do not match"
        })


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):

    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html', {
                'form' : AuthenticationForm,
                'error' : 'User or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('home')
