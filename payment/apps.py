# coding=utf-8
__author__ = 'berluskuni'
from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = u'payment'
    verbose_name = u'Оплата'

    def ready(self):
        import payment.signals