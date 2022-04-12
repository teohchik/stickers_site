from django.shortcuts import render, redirect
from django.db import transaction


from .services.add_order import add_order_func
from .services.bag import remove_item_from_bag, update_data_in_bag, creation_context


def bag(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            # Якщо в.юшка получає позиціонні аргументи, то виконуємо цю дію
            remove_item_id = request.GET.get('remove_item')
            if remove_item_id:
                user = request.user
                remove_item_from_bag(remove_item_id, user)
                return redirect('bag')

            context = creation_context(request)
            return render(request, "bag/bag.html", context)

        elif request.method == 'POST':
            update_data_in_bag(request)
            return redirect('bag')
    else:
        return render(request, "access_is_blocked.html")


def add_order(request):
    add_order_func(request)

    return redirect('bag')
