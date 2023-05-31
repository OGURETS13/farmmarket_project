import os

from django.contrib.auth import get_user_model
from django.shortcuts import (
    redirect,
    render,
    get_object_or_404,
    get_list_or_404
)

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content

from .models import Order, OrderItem

User = get_user_model()


def index(request):
    return render(request, 'index.html')


def order_paid(request):
    order = get_object_or_404(Order, pk=2)
    client = order.client
    order_items = get_list_or_404(OrderItem, order=order)
    items = []
    base_url = request.scheme + '://' + request.get_host()
    for item in order_items:
        image_url = base_url + item.product.image.url
        items.append({
            "name": item.product.name,
            "qty": item.quantity,
            "hst": '15%',
            "price": item.product.price * item.quantity,
            "image": image_url
        })
    print(item.product.image.url)
    message = Mail(
        from_email='frantsph@gmail.com',
        to_emails='Hdorkina@gmail.com',
    )

    message.template_id = 'd-9efc76d1199c443385e90c96825da47b'

    message.dynamic_template_data = {
        "order_number": order.pk,
        "first_name": client.first_name,
        "items": items,
        "shipping_address": order.address,
        "order_date": str(order.date.strftime('%Y-%m-%d %H:%M:%S')),
        "seller": order.farmer.username
    }

    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
    return redirect('mail:index')
