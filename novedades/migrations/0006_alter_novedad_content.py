# Generated by Django 4.2 on 2024-10-21 00:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0005_alter_novedad_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedad',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
