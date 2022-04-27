from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from api.order_management_api.serializers import OrderSerializer
from order_management.models import Order


class OrdersProcessingApiView(generics.ListAPIView):
    queryset = Order.objects.filter(status=1)
    serializer_class = OrderSerializer
    permission_classes = (IsAdminUser,)
