from order_management.models import Order


def get_orders_info():
    orders = Order.objects.all().order_by("-date")
    print(orders[2].status)
    return orders