from django.urls import path
from .views import storage_all, storage_dima_vlad

urlpatterns = [
    path('', storage_dima_vlad, name='storage_dima_vlad'),
    path('all_storage/', storage_all, name='storage_all'),
]
