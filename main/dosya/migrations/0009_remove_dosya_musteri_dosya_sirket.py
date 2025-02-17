# Generated by Django 5.1.5 on 2025-02-13 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosya', '0008_alter_dosyatürü_sene'),
        ('sirket', '0002_remove_sirket_calisanlar_sirket_calisanlar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosya',
            name='musteri',
        ),
        migrations.AddField(
            model_name='dosya',
            name='sirket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dosyalar', to='sirket.sirket'),
        ),
    ]
