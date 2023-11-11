from django.forms import ModelForm
from .models import Agricultural_product, Farmer
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class ProductForm(ModelForm):
    class Meta:
        model = Agricultural_product
        exclude = ('seller',)

class FarmerForm(ModelForm):
    class Meta:
        model = Farmer
        exclude = ('user', 'saldo')

class UserProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

    #def __init__(self, *args, **kwargs):
    #    super(UserProfileForm, self).__init__(*args, **kwargs)
    #    self.fields['email'].widget.attrs['readonly'] = True  # Si deseas hacer el campo de correo electrónico solo de lectura
