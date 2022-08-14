from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_409_CONFLICT
from django.contrib.auth.models import User
from api.bag_api.serializers import BagProductsSerializer, BagSerializer
from bag.models import BagProduct, Bag
from bag.services.add_order import add_order_func
from order_management.services.add_product_for_bag import check_bag


class BagProductsApiView(generics.ListCreateAPIView):
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
    order = add_order_func(pk)
    request_user = User.objects.get(pk=pk)

    check_bag(request_user)

    if order == 409:
        return Response(status=HTTP_409_CONFLICT)
    else:
        check_bag(request.user)
        return JsonResponse({"pk_order": f"{order}"})

