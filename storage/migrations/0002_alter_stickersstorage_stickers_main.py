# Generated by Django 4.0.3 on 2022-04-10 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stickersstorage',
            name='stickers_main',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='storage_stickers', to='storage.stickersmain', verbose_name='ID пака'),
        ),
    ]
