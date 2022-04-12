from django.contrib.auth.models import User

from bag.models import BagProduct, Bag
from storage.models import StickersStorage, StickersMain
from storage.services.storage import formatting_quantity


def creation_context(request):
    """
    Формування контексту
    """
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
    return context


def check_bag(user):
    try:
        bag = Bag.objects.get(pk=user)
        return bag
    except Bag.DoesNotExist:
        Bag.objects.create(user=user)


def add_product_for_bag_func(request, name, pk):
    """
    Додавання товару в корзину
    """
    # Додаємо товар до корзини
    product = StickersMain.objects.get(pk=pk)
    bag_user = request.user
    user_packing = User.objects.filter(username=name).get()

    bag = check_bag(bag_user)

    # Перевіряємо, чи є данний товар вже в корзині
    flag = BagProduct.objects.filter(product=product, user=user_packing, bag=bag)
    if not flag:
        BagProduct.objects.create(user=user_packing, product=product, bag=bag)
