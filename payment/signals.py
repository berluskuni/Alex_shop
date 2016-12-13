__author__ = 'berluskuni'
from django.shortcuts import get_object_or_404
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import payment_was_flagged, payment_was_successful
from order.models import Order


def payment_notification(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == "Completed":
        order = get_object_or_404(Order, id=ipn_obj.invoice)
        order.paid = True
        order.save()

payment_was_successful.connect(payment_notification)
payment_was_flagged.connect(payment_notification)