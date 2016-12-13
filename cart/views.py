# coding=utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from shop.models import Product
from .forms import CartAddProductForm
from .models import WishListProduct
from account.models import User
from django.contrib import auth


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart})


def cart_checkout(request):
    if request.user.is_authenticated():
        user = request.user
        return render(request, 'checkout.html', {'user': user})
    else:
        return render(request, 'checkout.html', {})


def wish_list_add(request, product_id):
    WishListProduct.objects.create(product_id=product_id)
    return redirect('cart:wish_list_detail')


def wish_list_detail(request):
    products = {}
    for i in WishListProduct.objects.all():
        products[i.product_id] = Product.objects.get(id=i.product_id)
    return render(request, 'wish_list.html', {'products': products})


def wish_list_remove(request, product_id):
    WishListProduct.objects.filter(product_id=product_id).delete()
    return redirect('cart:wish_list_detail')


def wish_list_cart_add(request, product_id):
    if cart_add(request, product_id):
        WishListProduct.objects.filter(product_id=product_id).delete()
        return redirect('cart:cart_detail')
    else:
        return redirect('cart:wish_list_detail')







