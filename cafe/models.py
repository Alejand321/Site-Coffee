from django.db import models

class Cafe(models.Model):
    nombre = models.CharField(max_length=300)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    imagen = models.CharField(max_length=2083)