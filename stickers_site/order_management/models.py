from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Запаковує', blank=True)
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
