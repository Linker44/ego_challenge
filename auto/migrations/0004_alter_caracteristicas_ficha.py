# Generated by Django 5.0.3 on 2024-03-10 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0003_alter_auto_ficha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caracteristicas',
            name='ficha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='caracteristicas', to='auto.ficha'),
        ),
    ]
