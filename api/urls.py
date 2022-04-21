from django.urls import path, include

from .storage_api.urls import product_patterns


urlpatterns = [
    path('v1/storage/', include(product_patterns)),
]

