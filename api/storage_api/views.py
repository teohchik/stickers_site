from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from api.storage_api.serializers import StorageQuantitySerializer, ProductsInfoSerializer
from storage.models import StickersStorage, StickersMain


class ProductsQuantityApiView(generics.ListAPIView):
    queryset = StickersStorage.objects.all()
    serializer_class = StorageQuantitySerializer
    permission_classes = (IsAdminUser,)


class ProductsInfoApiView(generics.ListAPIView):
    queryset = StickersMain.objects.filter(is_published=True).prefetch_related('storage_stickers')
    serializer_class = ProductsInfoSerializer
    permission_classes = (IsAdminUser,)


class ProductQusntityUpdateApiView(generics.RetrieveUpdateAPIView):
    queryset = StickersStorage.objects.all()
    serializer_class = StorageQuantitySerializer
    permission_classes = (IsAdminUser,)


class ProductQuantityApiView(generics.RetrieveAPIView):
    queryset = StickersStorage.objects.all()
    serializer_class = StorageQuantitySerializer
    permission_classes = (IsAdminUser,)


class ProductInfoApiView(generics.RetrieveAPIView):
    queryset = StickersMain.objects.filter(is_published=True)
    serializer_class = ProductsInfoSerializer
    permission_classes = (IsAdminUser,)