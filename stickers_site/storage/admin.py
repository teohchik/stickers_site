from django.contrib import admin
from .models import Category, StickersMain, StickersDima, StickersVlad


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


class StickersMainAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'total_quantity', 'quantity_in_pack', 'is_published', 'photo')


class StickersDimaAdmin(admin.ModelAdmin):
    list_display = ('stickers_main', 'quantity')


class StickersVladAdmin(admin.ModelAdmin):
    list_display = ('stickers_main', 'quantity')


admin.site.register(Category, CategoryAdmin)
admin.site.register(StickersMain, StickersMainAdmin)
admin.site.register(StickersDima, StickersDimaAdmin)
admin.site.register(StickersVlad, StickersVladAdmin)
