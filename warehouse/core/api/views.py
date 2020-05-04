from rest_framework.viewsets import ModelViewSet

from core.models import Order
from core.api.serializers import OrderModelSerializer


class OrderModelViewSet(ModelViewSet):
    """
    A simple CRUD view for orders
    """

    queryset = Order.objects.all()
    lookup_field = 'order_number'
    serializer_class = OrderModelSerializer
