# Generated by Django 5.1.5 on 2025-02-13 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dosya', '0010_dosya_degisiklik_tarihi_dosya_degisiklik_yapan_kisi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosya',
            name='ad',
        ),
    ]
