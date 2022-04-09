from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from storage.models import Category, StickersMain


class Bag(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, primary_key=True, verbose_name='Запаковує')
    price = models.IntegerField(verbose_name='Сума', blank=True, null=True)
    ttn = models.CharField(max_length=255, blank=True, null=True, verbose_name='ТТН')

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ['pk']


class BagProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, verbose_name='Категорія')
    product = models.ForeignKey(StickersMain, on_delete=models.CASCADE, verbose_name='Товар')
    bag = models.ForeignKey(Bag, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Замовлення')
    quantity = models.IntegerField(verbose_name='Кількість', default=0)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Запаковує')

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = 'Товар в корзину'
        verbose_name_plural = 'Товари в корзині'
        ordering = ['pk']