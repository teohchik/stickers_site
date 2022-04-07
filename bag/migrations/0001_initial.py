# Generated by Django 4.0.3 on 2022-04-07 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bag',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Запаковує')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Сума')),
                ('ttn', models.CharField(blank=True, max_length=255, null=True, verbose_name='ТТН')),
            ],
            options={
                'verbose_name': 'Корзина',
                'verbose_name_plural': 'Корзина',
                'ordering': ['pk'],
            },
        ),
    ]