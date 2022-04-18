from django.urls import path

from .storage_api.views import StorageQuantityApiView, ProductsInfoApiView

urlpatterns = [
    path('v1/storage_list/', StorageQuantityApiView.as_view()),
    path('v1/product_info_list/', ProductsInfoApiView.as_view()),
]
