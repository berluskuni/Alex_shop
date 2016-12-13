__author__ = 'berluskuni'

from django.conf.urls import url
from .views import coupon_apply


urlpatterns = [
    url(r'^apply', coupon_apply, name='apply')
]
