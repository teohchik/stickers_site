from django.urls import path

from .views import search_for_ttn

ttn_patterns = [
    path('<str:ttn>/', search_for_ttn),
]