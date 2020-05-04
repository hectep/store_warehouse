from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Order
from core.tasks import send_created_order


@receiver(post_save, sender=Order)
def send_order_to_warehouse(sender,created, instance, *args, **kwargs):
    """
    A signal that fires celery task to send order to warehouse
    """
    if created:
        send_created_order.delay(instance.pk)
