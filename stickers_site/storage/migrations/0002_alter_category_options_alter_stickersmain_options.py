# Generated by Django 4.0.3 on 2022-03-31 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='stickersmain',
            options={'verbose_name': 'Інфа про стікери', 'verbose_name_plural': 'Інфа про стікери'},
        ),
    ]
