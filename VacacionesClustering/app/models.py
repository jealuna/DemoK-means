"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Lugar(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    nombre = models.TextField()
    clusters = models.IntegerField()
 
    def __str__(self):
        return f'{self.nombre}'
