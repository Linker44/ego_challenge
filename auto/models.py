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
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/ficha/', null=True, blank=True)

    def __str__(self):
        return self.titulo


class Caracteristicas(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    ficha = models.ForeignKey(
        "Ficha", on_delete=models.CASCADE, related_name="caracteristicas")
    image = models.ImageField(
        upload_to='images/caracteristicas/', null=True, blank=True)

    def __str__(self):
        return self.titulo
