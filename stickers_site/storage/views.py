from django.shortcuts import render
from .models import StickersMain, StickersDima, StickersVlad


# Create your views here.


def storage_all(request):
    return render(request, 'storage/all_storage.html', {})


def storage_dima_vlad(request):
    storage_dima = StickersDima.objects.select_related('stickers_main').all()
    storage_vlad = StickersVlad.objects.select_related('stickers_main').all()

    formatting_quantity(storage_dima)
    formatting_quantity(storage_vlad)

    context = {
        "storages": [{'storage': storage_dima, 'owner_storage': 'Склад Діми'},
                     {'storage': storage_vlad, 'owner_storage': 'Склад Влада'}],
    }

    return render(request, 'storage/storage_dima_vlad.html', context)


def formatting_quantity(storage):
    for pack in storage:
        quantity = pack.quantity
        quantity_in_pack = pack.stickers_main.quantity_in_pack

        if quantity % quantity_in_pack == 0:
            pack.quantity = int(quantity/quantity_in_pack)
        else:
            pack.quantity = quantity/quantity_in_pack

