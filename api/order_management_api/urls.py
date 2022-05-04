from django.urls import path

from .views import OrdersProcessingApiView, OrderApiView, processing_to_done

order_patterns = [
    path('processing/', OrdersProcessingApiView.as_view()),
    path('<int:pk>/', OrderApiView.as_view()),
    path('processing_to_done/', processing_to_done),
]