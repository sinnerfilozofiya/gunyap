# Generated by Django 5.0 on 2024-06-06 14:30

import ckeditor.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hizmet', '0008_alter_hizmet_tanim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hizmet',
            name='ozet',
            field=ckeditor.fields.RichTextField(blank=True, default='Özet', null=True, validators=[django.core.validators.MaxLengthValidator(500)]),
        ),
    ]
