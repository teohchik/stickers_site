from django.contrib import admin

from bag.models import Bag, CustomUser


class BagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'price', 'ttn')


admin.site.register(Bag, BagAdmin)
admin.site.register(CustomUser)