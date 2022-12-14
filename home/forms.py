from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class ProductForm(ModelForm): 
  class Meta:
    model = models.Products
    fields = ['name', 'price', 'image','category']

class PackForm(ModelForm): 
  class Meta:
    model = models.Pack
    fields = '__all__'


class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'password1', 'password2']


class EditForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name']
    
    