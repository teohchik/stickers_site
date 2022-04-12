from django.shortcuts import render, redirect

from order_management.services.add_product_for_bag import creation_context, add_product_for_bag_func


def add_bag(request):
    if request.user.is_authenticated:
        context = creation_context(request)

        return render(request, 'order_management/add_bag.html', context)
    else:
        return render(request, 'access_is_blocked.html', {})


def add_product_for_bag(request, name, pk):
    add_product_for_bag_func(request, name, pk)
    return redirect('add_bag')
