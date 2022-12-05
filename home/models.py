from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.PositiveIntegerField(null=True)
    image = models.ImageField(upload_to='', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Pack(models.Model):
    name = models.CharField(max_length=100, null=True)
    products = models.ManyToManyField(Products, related_name='include', blank=True)
    price = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.body[0:50]
