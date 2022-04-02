from django.shortcuts import render

# Create your views here.


def order_management_command(request):
    return render(request, 'storage/order_management.html', {})