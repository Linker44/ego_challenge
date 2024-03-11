# Generated by Django 5.0.3 on 2024-03-11 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_alter_caracteristicas_ficha'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/autos/'),
        ),
        migrations.AddField(
            model_name='caracteristicas',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/caracteristicas/'),
        ),
        migrations.AddField(
            model_name='ficha',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/ficha/'),
        ),
    ]