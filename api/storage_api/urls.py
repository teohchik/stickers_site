from django.urls import path

from .views import ProductsQuantityApiView, ProductsInfoApiView, ProductQuantityApiView, ProductInfoApiView, \
    ProductQusntityUpdateApiView

product_patterns = [
    path('products_quantity/', ProductsQuantityApiView.as_view()),
    path('products_info/', ProductsInfoApiView.as_view()),
    path('product_quantity_update/<int:pk>/', ProductQusntityUpdateApiView.as_view()),
    path('product_quantity/<int:pk>/', ProductQuantityApiView.as_view()),
    path('product_info/<int:pk>/', ProductInfoApiView.as_view()),
]