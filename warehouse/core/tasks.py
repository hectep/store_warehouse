import requests

from warehouse.celery import app
from core.models import Order


@app.task()
def update_order_in_store(order_id):
    """
    A Celery task that updates order status in store.
    """
    order = Order.objects.get(id=order_id)
    data = {
        'status': order.status,
    }
    api_url = f'{order.store.web_address}/api/orders/{order.order_number}/'
    requests.patch(api_url, json=data)
