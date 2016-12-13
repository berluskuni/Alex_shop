# coding=utf-8
from django.db import models
from shop.models import Product


class WishListProduct(models.Model):
    product = models.ForeignKey(Product, verbose_name=u'имя продукта', blank=True, null=True)