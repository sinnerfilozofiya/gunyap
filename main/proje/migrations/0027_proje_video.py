# Generated by Django 5.0 on 2024-06-06 15:18

import proje.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0026_alter_proje_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='proje',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=proje.models.proje_video_path),
        ),
    ]
