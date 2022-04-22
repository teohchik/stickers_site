from django.db import models
from django.urls import reverse

from storage.models import Category, StickersMain


class Bag(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True, verbose_name='Запаковує')
    price = models.IntegerField(verbose_name='Сума', default=0)
    ttn = models.CharField(max_length=255, default=0, verbose_name='ТТН')

    def get_absolute_url(self):
        return reverse('bag')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ['pk']


class BagProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name='Категорія')
    product = models.ForeignKey(StickersMain, on_delete=models.CASCADE, verbose_name='Товар', related_name='product')
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Корзина',
                            related_name='bag_products')
    quantity = models.IntegerField(verbose_name='Кількість', default=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Запаковує')

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = 'Товар в корзину'
        verbose_name_plural = 'Товари в корзині'
        ordering = ['pk']
