# Generated by Django 5.0 on 2024-05-05 14:16

import kurumsal.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurumsal', '0011_madde_aciklama'),
    ]

    operations = [
        migrations.AddField(
            model_name='belgeler',
            name='belge',
            field=models.FileField(default='slider/isguvenligi.pdf', upload_to=kurumsal.models.document_directory_path),
        ),
    ]
