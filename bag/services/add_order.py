from django.db import transaction

from bag.models import Bag, BagProduct
from order_management.models import OrderProduct, Order
from storage.models import StickersStorage


@transaction.atomic
def add_order_func(request):
    # Створюємо замовлення і наповнюємо його даними з корзини
    bag = Bag.objects.filter(user=request.user).get()

    price = bag.price
    ttn = bag.ttn

    order = Order.objects.create(user=request.user, price=price, ttn=ttn)

    products_in_bag = BagProduct.objects.filter(bag=bag)

    for product in products_in_bag:
        category = product.category
        product_id = product.product
        quantity_in_bag = product.quantity
        user_to_pack = product.user

        request_user = f"admin_{request.user.username}"

        # Віднімаємо quantity в StickersStorage
        if request_user == 'admin_dima':
            product_id.storage_stickers.quantity_dima -= quantity_in_bag
        else:
            product_id.storage_stickers.quantity_vlad -= quantity_in_bag
        product_id.storage_stickers.save()

        OrderProduct.objects.create(category=category,
                                    product=product_id,
                                    order=order,
                                    quantity=quantity_in_bag,
                                    user=user_to_pack)
    bag.delete()
    return order
