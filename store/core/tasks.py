import requests
from django.conf import settings

from store.celery import app
from core.models import Order


@app.task()
def send_created_order(order_pk):
    """
    A Celery task that sends order to warehouse.
    """
    order = Order.objects.get(id=order_pk)

    data = {
        'order_number': order.order_number,
        'status': order.status,
        'store': {'name': settings.STORE_NAME}
    }
    api_url = order.warehouse.web_address + '/api/orders/'
    requests.post(api_url, json=data)
