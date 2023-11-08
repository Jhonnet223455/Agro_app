from django.forms import ModelForm
from .models import Agricultural_product, Farmer

class ProductForm(ModelForm):
    class Meta:
        model = Agricultural_product
        fields = ['name', 'description', 'price', 'stock', 'image', 'seller']  # Asegúrate de incluir todos los campos necesarios

class FarmerForm(ModelForm):
    class Meta:
        model = Farmer
        exclude = ('user', 'saldo')
