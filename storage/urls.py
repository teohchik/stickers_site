from django.urls import path
from .views import all_storage

urlpatterns = [
    path('', all_storage, name='all_storage'),
]
