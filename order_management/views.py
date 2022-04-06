from django.shortcuts import render, redirect
from storage.models import StickersStorage

from storage.views import formatting_quantity



def add_bag(request):


    storages = StickersStorage.objects.select_related('stickers_main').all()
    formatting_quantity(storages)

    context = {
        'storages': storages,
    }

    return render(request, 'order_management/add_bag.html', context)


def add_product_for_bag(request, name, pk):

    print(name, pk)
    return redirect('add_bag')


