# Generated by Django 5.0 on 2024-05-10 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hizmet', '0004_hizmet_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Açıklama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanim', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
