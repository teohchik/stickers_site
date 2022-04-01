from django.urls import path
from .views import storage_all

urlpatterns = [
    path('', storage_all, name='storage_all')
]
