# Generated by Django 5.0 on 2024-05-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurumsal', '0017_bizkimiz_e_katalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sayac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('müşteri', models.IntegerField(default=232)),
                ('proje', models.IntegerField(default=521)),
                ('çalışan', models.IntegerField(default=15)),
            ],
        ),
    ]
