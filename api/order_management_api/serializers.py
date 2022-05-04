from rest_framework import serializers

from order_management.models import Order, OrderProduct


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('product', 'quantity', 'user')


class OrderSerializer(serializers.ModelSerializer):
    order_products = OrderProductSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('pk', 'user', 'status', 'date', 'price', 'ttn', 'order_products')
