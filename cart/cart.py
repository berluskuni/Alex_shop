# coding=utf-8
__author__ = 'berluskuni'

from decimal import Decimal
from django.conf import settings
from shop.models import Product
from cupons.models import Cupon


class Cart(object):
    def __init__(self, request):
        # Initial cart for users
        self.session = request.session
        self.coupon_id = self.session.get('coupon_id')
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Save cart user in to session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1, 'price': str(product.price)}
        elif quantity == '':
            quantity = 1
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] = int(quantity)
        self.save()

    # save date in session
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # in session modified
        self.session.modified = True

    # delete product in cart
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # iteration for product
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['quantity'] = int(item['quantity'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    @property
    def coupon(self):
        if self.coupon_id:
            return Cupon.objects.get(id=self.coupon_id)
        return None

    def get_discount(self):
        if self.coupon:
            return (self.coupon.discount / Decimal('100')) * self.get_total_price()
        return Decimal('0')

    def get_total_price_after_discount(self):
        return self.get_total_price() - self.get_discount()

    def tax(self):
        if self.coupon:
            return self.get_total_price_after_discount()*20/100
        return self.get_total_price()*20/100

    def get_total_price_with_tax(self):
        if self.coupon:
            return self.get_total_price_after_discount() + self.tax()
        return self.get_total_price() + self.tax()


