
from django.urls import path
from .views import home, products, ProductList


urlpatterns = [
    path('', home, name='home'),    
    path('products/', ProductList.as_view(template_name = "Agro_app/products.html"), name='productList'),
]
