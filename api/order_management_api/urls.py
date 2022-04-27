from django.urls import path

from .views import OrdersProcessingApiView

order_patterns = [
    path('processing/', OrdersProcessingApiView.as_view()),

]