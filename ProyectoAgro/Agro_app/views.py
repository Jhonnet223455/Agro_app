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
def products(request):
    return render(request, 'Agro_app/products.html')

class ProductList(ListView):
    model = agricultural_product # Llamamos a la clase 'Usuario' que se encuentra en nuestro archivo 'models.py'

class ProductoCrear(SuccessMessageMixin, CreateView): 
    model = agricultural_product # Llamamos a la clase 'Usuario' que se encuentra en nuestro archivo 'models.py'
    form = agricultural_product # Definimos nuestro formulario con el nombre de la clase o modelo 'Usuario'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Usuarios' de nuestra Base de Datos 
    success_message = 'Producto Creado Correctamente!' # Mostramos este Mensaje luego de Crear una Usuario

    # Redireccionamos a la página principal luego de crear un registro o Usuario
    def get_success_url(self):        
        return reverse('readproduct') # Redireccionamos a la vista principal 'leer'
    
class ProductDetail(DetailView): 
    model = agricultural_product # Llamamos a la clase 'Usuario' que se encuentra en nuestro archivo 'models.py' 

class ProductUpdate(SuccessMessageMixin, UpdateView): 
    model = agricultural_product # Llamamos a la clase 'Usuario' que se encuentra en nuestro archivo 'models.py' 
    form = agricultural_product # Definimos nuestro formulario con el nombre de la clase o modelo 'Usuario' 
    fields = '__all__' # Le decimos a Django que muestre todos los campos de la tabla 'Usuarios' de nuestra Base de Datos 
    success_message = 'Producto Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Usuario 

    # Redireccionamos a la página principal luego de actualizar un registro o Usuario
    def get_success_url(self):               
        return reverse('readproduct') # Redireccionamos a la vista principal 'leer'
    
class ProductDelete(SuccessMessageMixin, DeleteView): 
    model = agricultural_product 
    form = agricultural_product
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o Usuario
    def get_success_url(self): 
        success_message = 'Producto Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar una Usuario 
        messages.success (self.request, (success_message))       
        return reverse('readproduct') # Redireccionamos a la vista principal 'leer'