# Generated by Django 5.0 on 2024-06-06 14:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hizmet', '0007_alter_hizmet_ozet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hizmet',
            name='tanim',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
