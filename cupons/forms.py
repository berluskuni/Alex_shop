__author__ = 'berluskuni'
from django import forms


class CuponApllyForm(forms.Form):
    coupon = forms.CharField()
