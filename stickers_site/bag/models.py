from django.db import models
from django.contrib.auth.models import User

from storage.models import Category, StickersMain


class Bag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Запаковує')
    price = models.IntegerField(verbose_name='Сума')
    ttn = models.CharField(max_length=255, blank=True, verbose_name='ТТН')

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'
        ordering = ['pk']


