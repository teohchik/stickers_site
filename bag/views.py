from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction

from .models import BagProduct, Bag
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
    else:
        return render(request, "access_is_blocked.html")


@transaction.atomic
def add_order(request):
    # Створюємо замовлення і наповнюємо його даними з корзини
    bag = Bag.objects.filter(user=request.user).get()

    price = bag.price
    ttn = bag.ttn

    # order = Order.objects.create(user=request.user, price=price, ttn=ttn)

    products_in_bag = BagProduct.objects.filter(bag=bag)

    for product in products_in_bag:
        category = product.category
        product_id = product.product
        quantity_in_bag = product.quantity
        user_to_pack = product.user

        users = {'admin_dima': 'quantity_dima', 'admin_vlad': 'quantity_vlad'}

        quantity_who = users[request.user.username]

        quantity_user = product_id.storage_stickers.quantity_who
        quantity_user -= int(quantity_in_bag)
        quantity_user.save()
        # StickersStorage.objects.filter(user=user_to_pack).get().update(quantity_who=F(f'{quantity_who}') - quantity_in_bag)

        # OrderProduct.objects.create(category=category,
        #                             product=product_id,
        #                             order=order,
        #                             quantity=quantity_in_bag,
        #                             user=user_to_pack)

    return redirect('bag')
