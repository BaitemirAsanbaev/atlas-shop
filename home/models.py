from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to='', null=True,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Pack(models.Model):
    name = models.CharField(max_length=100, null=True)
    products = models.ManyToManyField(Products, blank=True)
    image = models.ImageField(upload_to="", null=True)
    price = models.PositiveIntegerField(null=True)

    def get_products(self):
        return self.products.all()
        
    def __str__(self):
        return self.name


class Feedback(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.body[0:50]


class Cart(models.Model):
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Products, blank=True, related_name='products')
    def get_products(self):
        return self.products.all()
    def __str__(self):
        return str(self.id)
