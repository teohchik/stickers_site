from django.contrib import admin
from .models import Order, OrderProduct


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'status', 'date', 'price', 'ttn')


admin.site.register(Order, OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category', 'product', 'order', 'bag', 'quantity', 'user')


admin.site.register(OrderProduct, OrderProductAdmin)
