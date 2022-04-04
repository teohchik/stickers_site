from django.shortcuts import render
from storage.models import StickersStorage

from storage.views import formatting_quantity
from .forms import GetQuantityDimaForm, GetQuantityVladForm


def add_order(request):
    if request.method == 'POST':
        form_dima = GetQuantityDimaForm(request.POST)
        if form_dima.is_valid():
            print(form_dima.cleaned_data['quantity_dima'])
            print(form_dima.cleaned_data['product_pk'])

        form_vlad = GetQuantityVladForm(request.POST)
        if form_vlad.is_valid():
            print('OK_vlad')
    else:
        form_dima = GetQuantityDimaForm(request.POST)
        form_vlad = GetQuantityVladForm(request.POST)

    storages = StickersStorage.objects.select_related('stickers_main').all()
    formatting_quantity(storages)

    context = {
        'storages': storages,
        'forms': {'dima': form_dima, 'vlad': form_vlad}
    }

    return render(request, 'order_management/add_order.html', context)





