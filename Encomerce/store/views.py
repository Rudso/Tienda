from django.shortcuts import render, get_object_or_404
from .models import Category,Product

# Create your views here.

def index(request):
    
    all_product = Product.objects.all()
    categorys = Category.objects.all()
    context = {'category':categorys,'products':all_product}
    return render(request, "store.html",context)
        

def category(request):
    categorys = Category.objects.all()
    context = {'category':categorys}
    return render(request,"category.html",context)

def main_page(request):
    all_product = Product.objects.all()   
    context = {'products':all_product}
    return render(request, "main-product-section.html",context)

def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories':all_categories}


def list_categorys(request,category_slug=None):
    categor= get_object_or_404(Category,slug=category_slug)
    productos = Product.objects.filter(category=categor)
    return render(request,'list-category.html',{'categor':categor,'productos':productos})
    
        
def product_info(request, slug):
    product= get_object_or_404(Product,slug=slug)
    context = {'products':product}
    return render(request,'product-info.html',context)
    

