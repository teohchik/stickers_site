# Generated by Django 4.0.3 on 2022-04-09 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BagProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Кількість')),
                ('bag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bag.bag', verbose_name='Замовлення')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='storage.category', verbose_name='Категорія')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.stickersmain', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Запаковує')),
            ],
            options={
                'verbose_name': 'Товар в корзину',
                'verbose_name_plural': 'Товари в корзині',
                'ordering': ['pk'],
            },
        ),
    ]