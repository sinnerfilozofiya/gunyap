# Generated by Django 5.0 on 2024-05-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0003_alter_proje_baslik'),
    ]

    operations = [
        migrations.AddField(
            model_name='proje',
            name='eklenme_tarihi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
