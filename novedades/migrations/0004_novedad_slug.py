# Generated by Django 4.2 on 2024-10-20 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0003_remove_novedad_creator_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='novedad',
            name='slug',
            field=models.SlugField(default='', unique=True, verbose_name='Slug'),
        ),
    ]
