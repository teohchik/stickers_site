from django.urls import path
from .views import order_management_command

urlpatterns = [
    path('', order_management_command, name='order_management_command'),

]
