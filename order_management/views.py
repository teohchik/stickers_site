from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from bag.models import Bag, BagProduct
from order_management.models import OrderProduct
from storage.models import StickersStorage, StickersMain

from storage.views import formatting_quantity


def add_bag(request):
    if request.user.is_authenticated:
        storages = StickersStorage.objects.select_related('stickers_main').all()
        formatting_quantity(storages)

        # Получаємо список товарів, які вже в корзині
        bag = check_bag(request.user)
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
    else:
        return render(request, 'access_is_blocked.html', {})


def add_product_for_bag(request, name, pk):
    # Додаємо товар до корзини
    product = StickersMain.objects.get(pk=pk)
    bag_user = request.user
    user_packing = User.objects.filter(username=name).get()

    bag = check_bag(bag_user)

    # Перевіряємо, чи є данний товар вже в корзині
    flag = BagProduct.objects.filter(product=product, user=user_packing, bag=bag)
    if not flag:
        BagProduct.objects.create(user=user_packing, product=product, bag=bag)
    return redirect('add_bag')


def check_bag(user):
    try:
        bag = Bag.objects.get(pk=user)
        return bag
    except Bag.DoesNotExist:
        Bag.objects.create(user=user)