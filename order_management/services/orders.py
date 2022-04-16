from django.shortcuts import get_object_or_404

from order_management.models import Order


def get_orders_info():
    orders_info = Order.objects.all().order_by("-date")
    return orders_info


def get_order_info(pk):
    order_info = get_object_or_404(Order, pk=pk)
    return order_info
