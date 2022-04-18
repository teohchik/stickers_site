from rest_framework import serializers

from storage.models import StickersStorage, StickersMain


class StorageQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StickersStorage
        fields = ('stickers_main', 'quantity_dima', 'quantity_vlad',)


class ProductsInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StickersMain
        fields = ('title', 'total_quantity', 'quantity_in_pack', 'created_at', 'photo', 'category', 'is_published',)