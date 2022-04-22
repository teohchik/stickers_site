from rest_framework import serializers

from bag.models import BagProduct, Bag


class BagProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BagProduct
        fields = ('pk', 'product', 'bag', 'quantity', 'user')


class BagSerializer(serializers.ModelSerializer):
    bag_products = BagProductsSerializer(read_only=True, many=True)

    class Meta:
        model = Bag
        fields = ('pk', 'bag_products', 'price', 'ttn')
