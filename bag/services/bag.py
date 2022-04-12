from django.shortcuts import get_object_or_404, redirect

from bag.models import BagProduct, Bag
from order_management.services.add_product_for_bag import check_bag


def creation_context(request):
    """
    Формування контексту
    """

    bag_user = check_bag(request.user)
    storages = BagProduct.objects.select_related('product').filter(bag=bag_user)
    context = {
        'products_in_bag': storages,
        'bag': bag_user,
    }
    return context


def remove_item_from_bag(remove_item_id, user):
    """
    Видалення елементів з корзини, якщо був нажатий хрестик
    """

    remove_item = get_object_or_404(BagProduct, id=remove_item_id)
    remove_item.delete()

    # Якщо в корзині залишилось 0 елементів, то очищаємо поля "ttn" і "price"
    bag = Bag.objects.get(user=user)
    count_products = BagProduct.objects.filter(bag=bag).count()
    if count_products == 0:
        bag.ttn = "0"
        bag.price = 0
        bag.save()


def update_data_in_bag(request):
    """
    Оновлення корзини
    """

    # Видаляю ці ключі щоб залишились лише динамічні
    quantity_keys = list(request.POST.keys())
    quantity_keys.remove('csrfmiddlewaretoken')
    quantity_keys.remove('ttn')
    quantity_keys.remove('price')

    # Записую нові данні в БД
    for data_key in quantity_keys:
        new_quantity = request.POST.get(data_key)
        BagProduct.objects.filter(pk=data_key).update(quantity=new_quantity)

    new_ttn = request.POST.get('ttn')
    Bag.objects.filter(pk=request.user).update(ttn=new_ttn)

    new_price = request.POST.get('price')
    Bag.objects.filter(pk=request.user).update(price=new_price)

    return redirect('bag')
