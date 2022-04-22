from rest_framework import generics

from api.bag_api.serializers import BagProductsSerializer, BagSerializer
from bag.models import BagProduct, Bag


class BagProductsApiView(generics.ListAPIView):
    queryset = BagProduct.objects.all()
    serializer_class = BagProductsSerializer


class BagProductApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BagProduct.objects.all()
    serializer_class = BagProductsSerializer


class BagApiView(generics.RetrieveUpdateAPIView):
    queryset = Bag.objects.all().prefetch_related('bag_products')

    serializer_class = BagSerializer
