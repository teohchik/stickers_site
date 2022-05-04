from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser

from api.order_management_api.serializers import OrderSerializer
from order_management.models import Order


class OrdersProcessingApiView(generics.ListAPIView):
    queryset = Order.objects.filter(status=1)
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)


class OrderApiView(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)


@api_view(['GET'])
def processing_to_done(request):
    a = Order.objects.filter(status=1).update(status=2)
    return JsonResponse({"updated": f"{a}"})



