from rest_framework import serializers

from storage.models import StickersStorage, StickersMain


class StorageQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = StickersStorage
        fields = ('quantity_dima', 'quantity_vlad',)


class ProductsInfoSerializer(serializers.ModelSerializer):
    storage_stickers = StorageQuantitySerializer(read_only=True)

    class Meta:
        model = StickersMain
        fields = (
            'pk', 'storage_stickers', 'title', 'total_quantity', 'quantity_in_pack', 'photo')
