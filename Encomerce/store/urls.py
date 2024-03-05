from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index,name='store'),
    path('store/', views.index,name='store'),
    path('search/<slug:category_slug>/', views.list_categorys,name='categorys'),
    path('product/<slug:slug>/',views.product_info,name='products'),
]

