from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    feedback = models.Feedback.objects.all()

    data = {
        'feedback': feedback
    }
    return render(request, 'home.html', data)


def catalog(request):
  q = request.GET.get('q') if request.GET.get('q') != None else ''
  products = models.Products.objects.filter(category__name__icontains=q)
  packs = models.Pack.objects.all()
  categories = models.Category.objects.all()
  data = {
      'products': products,
      'categories': categories,
      'packs': packs
  }
  return render(request, 'catalog.html', data)

def add_product(request):
    form = forms.ProductForm
    if request.method == 'POST':
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    return render(request, 'create.html', {'form': form})

def from_low_to_high(request):
    products = list(models.Products.objects.all())
    categories = models.Category.objects.all()

    n = len(products)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if products[j].price > products[j + 1].price:
                swapped = True
                products[j], products[j + 1] = products[j + 1], products[j]

    data = {
        'products': products,
        'categories': categories
    }
    return render(request, 'catalog.html', data)


def from_high_to_low(request):
    products = list(models.Products.objects.all())
    categories = models.Category.objects.all()

    n = len(products)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if products[j].price < products[j + 1].price:
                products[j], products[j + 1] = products[j + 1], products[j]

    data = {
        'products': products,
        'categories': categories
    }
    return render(request, 'catalog.html', data)



@login_required(login_url='sign-in')
def cart(request):
    print(request)
    return render(request, 'cart.html')


def about(request):
  if request.method == 'POST':
    comment = models.Feedback.objects.create(author = request.user, body = request.POST.get('comment'))
    return redirect('home')

  return render(request, 'about.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def sign_in(request):
    page = 'signin'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Not correct')

    return render(request, 'login.html', {'page': page})


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error occured')
    return render(request, 'login.html', {'form': form})
