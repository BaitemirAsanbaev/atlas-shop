from django.urls import path
from . import views

urlpatterns = [
  path('sign-in/', views.sign_in, name='sign-in'),
  path('sign-up/', views.sign_up, name='sign-up'),
  path('logout/', views.logout_user, name='logout'),
  path('', views.index, name='home'),
  path('catalog/', views.catalog, name='catalog'),
  path('create/', views.add_product, name='create'),
  path('catalog/low-high', views.from_low_to_high, name='low-high'),
  path('catalog/high-low', views.from_high_to_low, name='high-low'),
  path('cart/', views.cart, name='cart'),
  path('about/', views.about, name='about'),
]