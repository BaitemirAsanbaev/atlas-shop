from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models


class ProductForm(ModelForm): 
  class Meta:
    model = models.Products
    fields = ['name', 'price', 'image','category']

class CategoryForm(ModelForm): 
  class Meta:
    model = models.Category
    fields = "__all__"

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'password1', 'password2']

    
    