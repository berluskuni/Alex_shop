__author__ = 'berluskuni'
from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.CharField(label='input_quantity', required=False)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


