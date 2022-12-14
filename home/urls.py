from django.urls import path
from . import views

urlpatterns = [
  path('sign-in/', views.sign_in, name='sign-in'),
  path('sign-up/', views.sign_up, name='sign-up'),
  path('logout/', views.logout_user, name='logout'),
  path('edit/', views.logout_user, name='edit-profile'),
  path('', views.index, name='home'),
  path('catalog/', views.catalog, name='catalog'),
  path('create/', views.ProductCreate.as_view(), name='create'),
  path('catalog/update/<int:id>', views.update_product, name='update'),
  path('catalog/delete/<int:id>', views.delete_product, name='delete'),
  path('catalog/low-high', views.from_low_to_high, name='low-high'),
  path('catalog/high-low', views.from_high_to_low, name='high-low'),
  path('cart/', views.cart, name='cart'),
  path('about/', views.about, name='about'),
  path('profile/', views.profile, name='profile'),
  path('profile/edit', views.edit_profile, name='edit'),
]