from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, StickersMain, StickersStorage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')


class StickersMainAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'total_quantity', 'quantity_in_pack', 'is_published', 'get_image')
    list_display_links = ('pk', 'title')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="100"')

    get_image.short_description = "Фото"


class StickersStorageAdmin(admin.ModelAdmin):
    list_display = ('stickers_main', 'quantity_dima', 'quantity_vlad')


admin.site.register(Category, CategoryAdmin)
admin.site.register(StickersMain, StickersMainAdmin)
admin.site.register(StickersStorage, StickersStorageAdmin)
