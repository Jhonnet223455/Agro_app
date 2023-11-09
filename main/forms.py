from django.forms import ModelForm
from .models import Agricultural_product, Farmer

class ProductForm(ModelForm):
    class Meta:
        model = Agricultural_product
        exclude = ('seller',)

class FarmerForm(ModelForm):
    class Meta:
        model = Farmer
        exclude = ('user', 'saldo')
