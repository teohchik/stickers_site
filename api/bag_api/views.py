from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from api.bag_api.serializers import BagProductsSerializer, BagSerializer
from bag.models import BagProduct, Bag


class BagProductsApiView(generics.ListAPIView):
    queryset = BagProduct.objects.all()
    serializer_class = BagProductsSerializer
    permission_classes = (IsAdminUser,)


class BagProductApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BagProduct.objects.all()
    serializer_class = BagProductsSerializer
    permission_classes = (IsAdminUser,)


class BagApiView(generics.RetrieveUpdateAPIView):
    queryset = Bag.objects.all().prefetch_related('bag_products')
    serializer_class = BagSerializer
    permission_classes = (IsAdminUser,)


@api_view(['GET'])
def create_order(request, pk):
    print(request.user)
    return Response(status=HTTP_200_OK)
