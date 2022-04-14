from order_management.models import Order


def get_orders_info():
    orders = Order.objects.all().order_by("-date")

    return orders