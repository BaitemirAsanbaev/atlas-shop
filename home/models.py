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

    def __str__(self):
        return self.name


class Feedback(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.body[0:50]


class Cart(models.Model):
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    products = models.ManyToManyField(Products, blank=True)
    def __str__(self):
        return str(self.client)

class Problems(models.Model):
    user = models.CharField(max_length=100)
    problem = models.TextField()

    def __str__(self):
        return self.problem[0:50]
