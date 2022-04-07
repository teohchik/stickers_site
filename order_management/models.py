from django.db import models
from django.contrib.auth.models import User
from storage.models import Category, StickersMain


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Запаковує')
    status = [
        (1, 'processing'),
        (2, 'success'),
        (3, 'error'),
    ]

    status = models.PositiveSmallIntegerField('Статус замовлення', choices=status, default=1)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата замовлення')
    price = models.IntegerField(verbose_name='Сума')
    ttn = models.CharField(max_length=255, blank=True, verbose_name='ТТН')

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
        ordering = ['pk']


class OrderProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    product = models.ForeignKey(StickersMain, on_delete=models.CASCADE, verbose_name='Товар')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, verbose_name='Замовлення')
    bag = models.BooleanField(verbose_name='В корзині?', default=True)
    quantity = models.IntegerField(verbose_name='Кількість')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Запаковує')

    def __str__(self):
        return f"{self.pk}"

    class Meta:
        verbose_name = 'Товар в замовлення'
        verbose_name_plural = 'Товари в замовленні'
        ordering = ['pk']