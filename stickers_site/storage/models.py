from django.db import models


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
        super().save(*args, **kwargs)  # Call the "real" save() method.
        StickersDima.objects.create(stickers_main_id=self.pk)
        StickersVlad.objects.create(stickers_main_id=self.pk)

    def __str__(self):
        return f"{self.pk} - {self.title}"

    class Meta:
        verbose_name = 'Інфу про стікери'
        verbose_name_plural = 'Інфа про стікери'


class StickersDima(models.Model):
    stickers_main = models.ForeignKey('StickersMain', on_delete=models.CASCADE, verbose_name='ID пака')
    quantity = models.IntegerField(default=0, verbose_name='Кількість у Діми')

    def __str__(self):
        return f"{self.pk} - {self.quantity}"

    class Meta:
        verbose_name = 'Склад Діми'
        verbose_name_plural = 'Склад Діми'


class StickersVlad(models.Model):
    stickers_main = models.ForeignKey('StickersMain', on_delete=models.CASCADE, verbose_name='ID пака')
    quantity = models.IntegerField(default=0, verbose_name='Кількість у Влада')

    def __str__(self):
        return f"{self.pk} - {self.quantity}"

    class Meta:
        verbose_name = 'Склад Влада'
        verbose_name_plural = 'Склад Влада'
