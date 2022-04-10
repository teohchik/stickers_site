from django.shortcuts import render

from django.urls import path
from .views import bag

urlpatterns = [
    path('bag/', bag, name='bag'),
]