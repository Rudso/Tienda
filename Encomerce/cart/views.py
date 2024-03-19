from django.shortcuts import render,get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse

# Create your views here.
def cart_index(request):
    return render(request, 'cart-summary.html')

def cart_add(request):
    cart=Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product,product_qty=product_quantity)
        cart.quantity= cart.__len__()
        
        response = JsonResponse({'qty':product_quantity})
        return response
    

def cart_delete(request):
    pass

def cart_update(request):
    pass