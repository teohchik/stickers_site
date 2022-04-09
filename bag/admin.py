from django.apps import AppConfig
from django.contrib import admin

from bag.models import Bag, BagProduct


class BagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'price', 'ttn')


admin.site.register(Bag, BagAdmin)


class BagProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category', 'product', 'bag', 'quantity', 'user',)


admin.site.register(BagProduct, BagProductAdmin)
