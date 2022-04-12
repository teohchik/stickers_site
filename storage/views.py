from django.shortcuts import render
from .models import StickersMain, StickersStorage

from .services.storage import creation_context


def all_storage(request):
    context = creation_context()
    return render(request, 'storage/all_storage.html', context)





