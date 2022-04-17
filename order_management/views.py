from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from order_management.forms import EditOrder
from order_management.services.add_product_for_bag import creation_context, add_product_for_bag_func
from order_management.services.orders import get_orders_info, get_order_info, get_items_in_order


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
    paginator = Paginator(orders_info, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_num_pages = paginator.num_pages

    context = {
        'orders_info': orders_info,
        'page_obj': page_obj,
        'page_num_pages': page_num_pages,
    }
    return render(request, 'order_management/orders.html', context)


def order(request, pk):
    order_info = get_order_info(pk)
    items_in_order = get_items_in_order(pk)

    if request.method == 'GET':
        form = EditOrder(instance=order_info)
    else:
        form = EditOrder(request.POST, instance=order_info)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {
        'order': order_info,
        'form': form,
        'items_in_order': items_in_order,
    }
    return render(request, 'order_management/order.html', context)
