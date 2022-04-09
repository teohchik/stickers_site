from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from bag.models import Bag, BagProduct
from order_management.models import OrderProduct
from storage.models import StickersStorage, StickersMain

from storage.views import formatting_quantity


def add_bag(request):
    storages = StickersStorage.objects.select_related('stickers_main').all()
    formatting_quantity(storages)

    # Получаємо список товарів, які вже в корзині
    bag = Bag.objects.get(pk=request.user)
    product_in_bag = BagProduct.objects.filter(bag=bag).values("product", "user")

    product_in_bag_dima = []
    product_in_bag_vlad = []
    for el in product_in_bag:
        if el['user'] == 1:
            product_in_bag_dima.append(el["product"])
        else:
            product_in_bag_vlad.append(el["product"])

    context = {
        'storages': storages,
        'product_in_bag_dima': product_in_bag_dima,
        'product_in_bag_vlad': product_in_bag_vlad,
    }

    return render(request, 'order_management/add_bag.html', context)


def add_product_for_bag(request, name, pk):
    user = request.user
    try:
        bag = Bag.objects.get(pk=user)
    except Bag.DoesNotExist:
        bag = Bag.objects.create(user=user)

    # Додаємо товар до корзини
    product = StickersMain.objects.get(pk=pk)
    user = User.objects.filter(username=name).get()

    # Перевіряємо, чи є данний товар вже в корзині
    flag = BagProduct.objects.filter(product=product, user=user, bag=True)
    if not flag:
        BagProduct.objects.create(user=user, product=product, bag=bag)

    return redirect('add_bag')
