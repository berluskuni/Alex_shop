# coding=utf-8
__author__ = 'berluskuni'
from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def task_order_created(order_id):
    """
    Отправка Email сообщения о создании покупке
    """
    order = Order.objects.get(id=order_id)
    subject = u'Заказ c номером {}'.format(order.id)
    message = u'Дорогой, {}, вы успешно сделали заказ.\
               Номер вашего заказа {}'.format(order.first_name, order.id)
    mail_send = send_mail(subject, message, 'berluskuni@gmail.com', [order.email])
    return mail_send
