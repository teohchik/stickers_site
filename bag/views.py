from django.shortcuts import render, redirect, get_object_or_404

from bag.models import BagProduct
from order_management.views import check_bag


def bag(request):
    if request.user.is_authenticated:
        if request.method == "GET":
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

    else:
        return render(request, "access_is_blocked.html")