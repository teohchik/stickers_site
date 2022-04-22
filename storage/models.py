from django.db import models
from django.shortcuts import get_object_or_404


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'


class StickersMain(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    total_quantity = models.IntegerField(verbose_name='Загальна кількість', default=0)
    quantity_in_pack = models.IntegerField(verbose_name='В паці', default=50)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публікації')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фото')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категорія')
    is_published = models.BooleanField(default=True, verbose_name='Опубліковано?')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        flag = get_object_or_404(StickersMain, pk=self.pk)
        if flag:
            StickersStorage.objects.create(stickers_main_id=self.pk)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = 'Інфу про стікери'
        verbose_name_plural = 'Інфа про стікери'
        ordering = ['pk']


class StickersStorage(models.Model):
    stickers_main = models.OneToOneField('StickersMain', on_delete=models.CASCADE, verbose_name='ID пака',
                                         related_name='storage_stickers')
    quantity_dima = models.IntegerField(default=0, verbose_name='Кількість у Діми')
    quantity_vlad = models.IntegerField(default=0, verbose_name='Кількість у Влада')

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = 'Склад стікерів'
        verbose_name_plural = 'Склад стікерів'
        ordering = ['stickers_main']


