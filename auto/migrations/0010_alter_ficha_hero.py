# Generated by Django 5.0.3 on 2024-03-11 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0009_alter_ficha_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='hero',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ficha', to='auto.hero'),
        ),
    ]
