# Generated by Django 5.0.3 on 2024-03-11 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0005_auto_image_caracteristicas_image_ficha_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Caracteristicas',
            new_name='Caracteristica',
        ),
    ]