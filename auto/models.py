from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.


class Auto(models.Model):
    TIPOS = [('auto', 'Auto'), ('pickup', 'Pickup'), ('comercial',
                                                      'Comercial'), ('suv', 'SUV'), ('crossover', 'Cross Over')]

    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=100, choices=TIPOS)
    fecha_auto = models.DateField(verbose_name='Fecha del modelo')
    precio = models.IntegerField(validators=[MinValueValidator(0)])
    ficha = models.OneToOneField(
        "Ficha", on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='images/autos/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class Ficha(models.Model):
    hero = models.OneToOneField(
        "Hero", on_delete=models.SET_NULL, null=True, blank=True, related_name="ficha")

    def __str__(self):
        name = f"Ficha self.id"
        if self.hero:
            name = f"Ficha {self.hero.pre_titulo}"
        return name


class Hero(models.Model):
    pre_titulo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    image = models.ImageField(
        upload_to='images/ficha/hero', null=True, blank=True)

    def __str__(self):
        return self.titulo


class Caracteristica(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    image = models.ImageField(
        upload_to='images/ficha/caractericas', null=True, blank=True)
    ficha = models.ForeignKey(
        "Ficha", on_delete=models.CASCADE, related_name="caracteristicas")

    def __str__(self):
        return self.titulo


class Prestacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    image = models.ImageField(
        upload_to='images/ficha/prestaciones', null=True, blank=True)
    ficha = models.ForeignKey(
        "Ficha", on_delete=models.CASCADE, related_name="prestaciones")

    def __str__(self):
        return self.titulo
