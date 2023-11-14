"""
URL configuration for agroblock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('unauthorized/', views.unauthorized, name='unauthorized'),
    path('profile/', views.profile, name='profile'),
    path('farmers/', views.profile, name='farmers'),
    path('farmers/register', views.farmer_register, name='farmer_register'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('products/', views.products, name='products'),
    path('products/create', views.product_create, name='product_create'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/<int:product_id>/delete', views.product_delete, name='product_delete'),
    path('products/edit/<int:product_id>', views.product_edit, name='product_edit'),
    path('shopping-cart/payment/', views.payment, name='payment'),
    path('shopping-cart/add/<int:product_id>', views.add_to_cart, name='add_to_cart'),
    path('buy/<int:product_id>', views.buy, name='buy'),
    path('shopping-cart/subtract/<int:product_id>', views.subtract_from_cart, name='subtract_from_cart'),
    path('shopping-cart/delete/<int:product_id>', views.delete_from_cart, name='delete_from_cart'),
    path('shopping-cart/clear', views.clear_cart, name='clear_cart'),


]