__author__ = 'berluskuni'
from .cart import Cart
from .models import WishListProduct


def cart(request):
    return {'cart': Cart(request)}


def wish_list(request):
    return {'wish_list': len(WishListProduct.objects.all())}
