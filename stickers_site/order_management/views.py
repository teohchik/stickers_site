from django.shortcuts import render
from storage.models import StickersStorage
from storage.forms import StickersStorage
from storage.views import formatting_quantity
from .forms import GetQuantityDimaForm


def add_order(request):
    if request.method == 'POST':
        form = GetQuantityDimaForm(request.POST)
        if form.is_valid():
            print('OK')
    else:
        form = GetQuantityDimaForm()

    storage_dima = StickersStorage.objects.select_related('stickers_main').all()

    formatting_quantity(storage_dima)



    context = {
        "storages": [{'storage': storage_dima, 'owner_storage': 'Склад Діми', 'form': form},
                     {'storage': storage_dima, 'owner_storage': 'Склад Влада', 'form': form}],
    }

    return render(request, 'order_management/add_order.html', context)





