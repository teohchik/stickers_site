from django.shortcuts import render
from .models import StickersMain, StickersDima

# Create your views here.

def storage_all(request):
    return render(request, 'storage/all_storage.html', {})


def storage_dima_vlad(request):
    storage_dima = StickersDima.objects.all()

    for pack in storage_dima:
        quantity = pack.quantity
        quantity_in_pack = pack.stickers_main.quantity_in_pack
        print(quantity, quantity_in_pack)

        if quantity % quantity_in_pack == 0:
            pack.quantity = int(quantity/quantity_in_pack)
        else:
            pack.quantity = quantity/quantity_in_pack

    storage_vlad = StickersDima.objects.all()
    context = {
        "storage_dima": storage_dima,
        "storage_vlad": storage_vlad
    }

    return render(request, 'storage/storage_dima_vlad.html', context)
