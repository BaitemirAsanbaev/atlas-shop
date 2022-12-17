from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import generic


def index(request):
    feedback = models.Feedback.objects.all()
    return render(request, 'home.html', {'feedback': feedback})


def catalog(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    products = models.Products.objects.filter(category__name__icontains=q)
    categories = models.Category.objects.all()

    if request.method == 'POST':
        if request.user.is_authenticated:
            cart_obj = models.Cart.objects.create(client=request.user)
            added = models.Products.objects.filter(id=request.POST.get('prod'))
            cart_obj.products.set(added)
        else:
            return redirect('sign-in')
    data = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'catalog.html', data)


class ProductCreate(generic.CreateView):
    template_name = 'create.html'
    form_class = forms.ProductForm
    queryset = models.Products.objects.all()
    success_url = '/catalog/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ProductCreate, self).form_valid(form=form)


def update_product(request, id):
    product = models.Products.objects.get(id=id)
    form = forms.ProductForm(instance=product)
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('catalog')
    return render(request, 'update.html', {'form': form})


def delete_product(request, id):
    product = models.Products.objects.get(id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('catalog')
    return render(request, 'delete.html', {'obj': product})


def from_low_to_high(request):
    products = list(models.Products.objects.all())
    categories = models.Category.objects.all()

    # bubble search
    n = len(products)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if products[j].price > products[j + 1].price:
                products[j], products[j + 1] = products[j + 1], products[j]

    data = {
        'products': products,
        'categories': categories
    }
    return render(request, 'catalog.html', data)


def from_high_to_low(request):
    products = list(models.Products.objects.all())
    categories = models.Category.objects.all()

    # bubble search
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
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error occured')
    return render(request, 'login.html', {'form': form})


@login_required(login_url='sign-in')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='sign-in')
def edit_profile(request):
    user = request.user
    form = forms.SignUpForm(instance=user)
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render(request, 'edit.html', {'form': form})


@login_required(login_url='sign-in')
def cart(request):
    cart = models.Cart.objects.all()
    new_cart = []
    for item in cart:
        if item.client == request.user:
            new_cart.insert(0, item)
    if request.method == 'POST':
        current_cart = models.Cart.objects.get(id=request.POST.get('del'))
        current_cart.delete()
    data = {
        'cart': new_cart,
        'not_null': len(new_cart)
    }

    return render(request, 'cart.html', data)


@login_required(login_url='sign-in')
def clear(request):
    cart = models.Cart.objects.all()

    for item in cart:
        if request.user == item.client:
            item.delete()
    return redirect('home')


def about(request):
    if request.method == 'POST':
        models.Feedback.objects.create(
            author=request.user.first_name, body=request.POST.get('comment'))
        return redirect('home')

    return render(request, 'about.html')


@login_required(login_url='sign-in')
def clients(request):
    problem = models.Problems.objects.all()

    return render(request, 'problems.html', {'problems': problem})

@login_required(login_url='sign-in')
def problem(request):
    if request.method == 'POST':
        models.Problems.objects.create(user=request.user.first_name, problem=request.POST.get('problem'))
        return redirect('home')

    return render(request, 'feedback.html')

def clear_problems(request):
    problems = models.Problems.objects.all()
    for i in problems:
        i.delete()
    return redirect('clients')

