from rest_framework import generics

from api.storage_api.serializers import StorageQuantitySerializer, ProductsInfoSerializer
from storage.models import StickersStorage, StickersMain


class StorageQuantityApiView(generics.ListAPIView):
    queryset = StickersStorage.objects.all()
    serializer_class = StorageQuantitySerializer


class ProductsInfoApiView(generics.ListAPIView):
    queryset = StickersMain.objects.filter(is_published=True).prefetch_related('storage_stickers')
    serializer_class = ProductsInfoSerializer
