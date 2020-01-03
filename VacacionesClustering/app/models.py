"""
Definition of models.
"""

from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Lugar(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()
    nombre = models.TextField()
    clusters = models.PositiveIntegerField(validators=[MinValueValidator(1)])
 
    def __str__(self):
        return f'{self.nombre}'
