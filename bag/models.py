from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


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


