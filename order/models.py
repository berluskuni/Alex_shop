# coding=utf-8
# Create your models here.

from django.db import models
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(verbose_name=u'Имя', max_length=50, blank=True, null=True)
    last_name = models.CharField(verbose_name=u'Фамилия', max_length=50, blank=True, null=True)
    email = models.EmailField(verbose_name=u'Email')
    address = models.CharField(verbose_name=u'Адрес', max_length=250, blank=True, null=True)
    postal_code = models.CharField(verbose_name=u'Почтовый код', max_length=20, blank=True, null=True)
    city = models.CharField(verbose_name=u'Город', max_length=100, blank=True, null=True)
    created = models.DateTimeField(verbose_name=u'Создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name=u'Обновлен', auto_now=True)
    paid = models.BooleanField(verbose_name=u'Оплачен', default=False)

    class Meta:
        db_table = 'db_orders'
        ordering = ('-created', )
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

    def __unicode__(self):
        return 'Заказ: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    class Meta:
        db_table = 'db_orders_items'
    order = models.ForeignKey(Order, related_name=u'items')
    product = models.ForeignKey(Product, related_name=u'order_items')
    price = models.DecimalField(verbose_name=u'Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name=u'Количество', default=1)

    def __unicode__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
