from django.urls import path, include

from .bag_api.urls import bag_patterns
from .storage_api.urls import product_patterns


urlpatterns = [
    path('v1/storage/', include(product_patterns)),
    path('v1/bag/', include(bag_patterns)),
]

