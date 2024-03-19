from django.contrib import admin
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_index,name='cart-index'),
    path('add/', views.cart_add,name='cart_add'),
    path('delete/', views.cart_delete,name='cart-delete'),
    path('update/', views.cart_update,name='cart-update'),
    
]