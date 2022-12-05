from django.forms import ModelForm
from . import models

class ProductForm(ModelForm):
  class Meta:
    model = models.Products
    fields = '__all__'