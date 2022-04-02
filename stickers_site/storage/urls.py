from django.urls import path
from .views import all_storage, order_management

urlpatterns = [
    path('', all_storage, name='all_storage'),
    path('order_management/', order_management, name='order_management'),

]
