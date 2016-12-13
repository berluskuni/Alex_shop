# coding=utf-8
from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import task_order_created
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('admin/orders/order/pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=order_{}.pdf'.format(order.id)
    weasyprint.HTML(string=html).write_pdf(response)
    return response


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})



def order_create(request):
    cart = Cart(request)
    user = request.user
    if request.method == 'POST' and user.is_authenticated():
        first_name = user.first_name
        last_name = user.last_name
        email = user.email
        address = user.address
        postal_code = user.post_code
        city = user.city

        order = Order.objects.create(first_name=first_name, last_name=last_name,
                                     email=email, address=address, postal_code=postal_code,
                                     city=city)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        task_order_created.delay(order.id)
        request.session['order_id'] = order.id
        return redirect(reverse('payment:process'))
    elif request.method == 'POST' and not user.is_authenticated():
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            task_order_created.delay(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
        else:
            errors = 'No create order form not is valid'
            return render(request, 'confirm_order.html', {'errors': errors})

    else:
        errors = 'No create order form not is valid'
        return render(request, 'confirm_order.html', {'errors': errors})



