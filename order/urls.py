__author__ = 'berluskuni'
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/', views.order_create, name='order_create'),
    url(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='AdminOrderDetail'),
    url(r'^admin/order/(?P<order_id>\d+)/pdf/$', views.admin_order_pdf, name='AdminOrderPDF'),
]
