# Generated by Django 4.2 on 2024-10-21 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0004_novedad_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedad',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Slug'),
        ),
    ]
