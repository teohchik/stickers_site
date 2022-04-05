from django.contrib import admin

from bag.models import Bag


class BagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'price', 'ttn')


admin.site.register(Bag, BagAdmin)