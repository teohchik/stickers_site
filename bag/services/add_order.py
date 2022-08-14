from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.status import HTTP_409_CONFLICT

from bag.models import Bag, BagProduct
from order_management.models import OrderProduct, Order
from storage.models import StickersStorage


def add_order_func(user):
    # Створюємо замовлення і наповнюємо його даними з корзини
    if type(user) == int:
        user = User.objects.get(pk=user)
    bag = Bag.objects.filter(user=user).get()

    price = bag.price
    ttn = bag.ttn

    order = Order(user=user, price=price, ttn=ttn)

    products_in_bag = BagProduct.objects.filter(bag=bag)

    for product in products_in_bag:
        category = product.category
        product_id = product.product
        quantity_in_bag = product.quantity
        user_to_pack = product.user

        # Віднімаємо quantity в StickersStorage
        if user_to_pack.username == 'dima':
            if product_id.storage_stickers.quantity_dima - quantity_in_bag >= 0:
                product_id.storage_stickers.quantity_dima -= quantity_in_bag
            else:
                transaction.rollback()
                return HTTP_409_CONFLICT

        else:
            if product_id.storage_stickers.quantity_vlad - quantity_in_bag >= 0:
                product_id.storage_stickers.quantity_vlad -= quantity_in_bag
            else:
                transaction.rollback()
                return HTTP_409_CONFLICT

        order.save()
        product_id.storage_stickers.save()
        OrderProduct.objects.create(category=category,
                                    product=product_id,
                                    order=order,
                                    quantity=quantity_in_bag,
                                    user=user_to_pack)

    bag.delete()
    return order
