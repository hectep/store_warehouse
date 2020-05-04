from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models import Order
from core.tasks import update_order_in_store


@receiver(post_save, sender=Order)
def send_order_to_store(
        sender, update_fields, created, instance, *args, **kwargs):
    """
    A signal that fires celery task to update order in store
    """

    if not created:
        update_order_in_store.delay(instance.pk)
