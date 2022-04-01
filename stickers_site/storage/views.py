from django.shortcuts import render


# Create your views here.

def storage_all(request):
    return render(request, 'storage/all_storage.html', {})
