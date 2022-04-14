from django.shortcuts import render, redirect

from order_management.services.add_product_for_bag import creation_context, add_product_for_bag_func
from order_management.services.orders import get_orders_info


def add_bag(request):
    if request.user.is_authenticated:
        context = creation_context(request)

        return render(request, 'order_management/add_bag.html', context)
    else:
        return render(request, 'access_is_blocked.html', {})


def add_product_for_bag(request, name, pk):
    add_product_for_bag_func(request, name, pk)
    return redirect('add_bag')


def orders(request):
    orders_info = get_orders_info()
    context = {'orders_info': orders_info}
    return render(request, 'order_management/orders.html', context)
