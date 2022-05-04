from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from api.order_management_api.serializers import OrderSerializer
from order_management.models import Order


@api_view(['GET'])
def search_for_ttn(request, ttn):
    order = Order.objects.filter(ttn=ttn).prefetch_related('order_products')
    if not order:
        return Response(status=HTTP_404_NOT_FOUND)

    serializer = OrderSerializer(order, many=True)
    return JsonResponse(serializer.data, safe=False)

