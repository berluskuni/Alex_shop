__author__ = 'berluskuni'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^remove/(?P<product_id>\d+)/', views.cart_remove, name='cart_remove'),
    url(r'^add/(?P<product_id>\d+)/', views.cart_add, name='cart_add'),
    url(r'^checkout/', views.cart_checkout, name='cart_checkout'),
    url(r'^wish_list/', views.wish_list_detail, name='wish_list_detail'),
    url(r'^wish_list_add/(?P<product_id>\d+)/', views.wish_list_add, name='wish_list_add'),
    url(r'^wish_list_remove/(?P<product_id>\d+)/', views.wish_list_remove, name='wish_list_remove'),
    url(r'wish_list_cart_add/(?P<product_id>\d+)/', views.wish_list_cart_add, name='wish_list_cart_add'),


]