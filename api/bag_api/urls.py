from django.urls import path

from .views import BagProductsApiView, BagApiView, BagProductApiView

bag_patterns = [
    path('bag_products/', BagProductsApiView.as_view()),
    path('bag_product/<int:pk>', BagProductApiView.as_view()),
    path('detail/<int:pk>', BagApiView.as_view()),
]