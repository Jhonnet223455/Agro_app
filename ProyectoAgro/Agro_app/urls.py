from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),    
    path('products/', ProductList.as_view(template_name = "Agro_app/products/products.html"), name='productList'), 
    path('products/productDetail/<int:pk>', ProductDetail.as_view(template_name = "Agro_app/products/details.html"), name='productDetails'),
    path('products/productCreate', ProductoCreate.as_view(template_name = "Agro_app/products/create.html"), name='productCreate'),
    #path('products/productEdit/<int:pk>', ProductUpdate.as_view(template_name = "Agro_app/products/update.html"), name='productUpdate'), 
    path('products/productDelete/<int:pk>', ProductDelete.as_view(), name='productDelete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)