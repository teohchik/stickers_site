from django.urls import path
from .views import add_order, add_product_for_cart

urlpatterns = [
    path('add_order/', add_order, name='add_order'),
    path('add_order/<str:name>/<int:pk>/', add_product_for_cart, name='add_product_for_cart'),

]
