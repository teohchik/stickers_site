from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from bag.models import Bag
from order_management.models import OrderProduct
from storage.models import StickersStorage, StickersMain

from storage.views import formatting_quantity


def add_bag(request):
    storages = StickersStorage.objects.select_related('stickers_main').all()
    formatting_quantity(storages)

    print(storages[1])

    context = {
        'storages': storages,
    }

    return render(request, 'order_management/add_bag.html', context)


def add_product_for_bag(request, name, pk):
    user = request.user
    try:
        Bag.objects.get(pk=user)
    except Bag.DoesNotExist:
        Bag.objects.create(user=user)

    # Додаємо товар до корзини
    product = StickersMain.objects.get(pk=pk)

    user = User.objects.filter(username=name).get()

    # Перевіряємо, чи є данний товар вже в корзині
    flag = OrderProduct.objects.filter(product=product, user=user, bag=True)
    if not flag:
        OrderProduct.objects.create(user=user, product=product)
        print("Додали до корзини")

    return redirect('add_bag')
