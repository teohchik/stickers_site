from django.shortcuts import render, redirect, get_object_or_404

from .models import BagProduct, Bag
from order_management.views import check_bag


def bag(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            # Видалення елементів, якщо був нажатий хрестик
            remove_item_id = request.GET.get('remove_item')
            if remove_item_id:
                remove_item = get_object_or_404(BagProduct, id=remove_item_id)
                remove_item.delete()
                return redirect('bag')
            bag_user = check_bag(request.user)

            storages = BagProduct.objects.select_related('product').filter(bag=bag_user)

            context = {
                'products_in_bag': storages,
                'bag': bag_user,
            }
            return render(request, "bag/bag.html", context)

        elif request.method == 'POST':
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
    else:
        return render(request, "access_is_blocked.html")