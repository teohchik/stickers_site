from django.urls import path
from .views import add_bag, add_product_for_bag

urlpatterns = [
    path('add_bag/', add_bag, name='add_bag'),
    path('add_bag/<str:name>/<int:pk>/', add_product_for_bag, name='add_product_for_bag'),

]
