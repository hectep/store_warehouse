from rest_framework.serializers import ModelSerializer, CharField

from core.models import Order, Store


class StoreSerializer(ModelSerializer):

    class Meta:
        model = Store
        fields = ('name', )


class OrderModelSerializer(ModelSerializer):
    store = StoreSerializer()

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        """
        Only name of a store is transferred so we need to
        deserialize it into proper warehouse instance
        """
        store_name = validated_data.pop('store')['name']
        store = Store.objects.filter(name=store_name).first()
        order_instance = Order.objects.create(**validated_data, store=store)
        return order_instance
