from django.db import models


STATUS_CHOICES = (
    ('new', 'New'),
    ('in_process', 'In process'),
    ('shipped', 'Shipped'),
)


class Store(models.Model):
    """
    General information about stores.
    web_address should be in format "http://address.com" without trailing slash
    """
    name = models.CharField(max_length=100)
    web_address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Order(models.Model):
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    order_number = models.CharField(max_length=15)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self):
        return f'ORDER {self.order_number} - {self.store} - {self.status}'
