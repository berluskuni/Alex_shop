from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Cupon
from .forms import CuponApllyForm


@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CuponApllyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['coupon']
        try:
            coupon = Cupon.objects.get(code__iexact=code,
                                       valid_from__lte=now,
                                       valid_to__gte=now,
                                       active=True)
            request.session['coupon_id'] = coupon.id
        except Cupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')