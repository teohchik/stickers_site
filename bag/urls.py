from django.shortcuts import render

from django.urls import path
from .views import bag, add_order

urlpatterns = [
    path('bag/', bag, name='bag'),
    path('bag/add_order/', add_order, name='add_order'),
]