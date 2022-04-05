from django.shortcuts import render, redirect
from storage.models import StickersStorage

from storage.views import formatting_quantity
from .forms import GetQuantityDimaForm, GetQuantityVladForm


def add_order(request):
    if request.method == 'POST':
        form_dima = GetQuantityDimaForm(request.POST)
        if form_dima.is_valid():
            print(form_dima.cleaned_data['quantity_dima'])

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


def add_product_for_cart(request, name, pk):
    form_dima = GetQuantityDimaForm(request.POST)
    if form_dima.is_valid():
        print(form_dima.cleaned_data['quantity_dima'])
    print(name, pk)
    return redirect('add_order')


