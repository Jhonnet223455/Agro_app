from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import agricultural_product
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from django import forms

# Create your views here.
def home(request):
    return render(request, 'Agro_app/home.html')

#@login_required
class ProductList(ListView):
    model = agricultural_product 

class ProductoCreate(SuccessMessageMixin, CreateView): 
    model = agricultural_product 
    form = agricultural_product
    fields = "__all__" 
    success_message = 'Producto Creado Correctamente!' 

    # Redireccionamos a la página principal luego de crear un registro
    def get_success_url(self):        
        return reverse('productList') # Redireccionamos a la vista principal 'leer'
    
class ProductDetail(DetailView): 
    model = agricultural_product 

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = agricultural_product 
    form = agricultural_product 
    fields = '__all__'
    success_message = 'Producto Actualizado Correctamente !' 

    # Redireccionamos a la página principal luego de actualizar un registro
    def get_success_url(self):               
        return reverse('productList') # Redireccionamos a la vista principal 'leer'
    
class ProductDelete(SuccessMessageMixin, DeleteView): 
    model = agricultural_product 
    form = agricultural_product
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' 
        messages.success (self.request, (success_message))       
        return reverse('productList') # Redireccionamos a la vista principal 'leer'