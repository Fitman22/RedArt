from django.db import models
from Ilustracion.models import Ilustracion
from Genero.models import Genero

class IlustracionGenero(models.Model):
    ilustracion = models.ForeignKey(Ilustracion, on_delete=models.CASCADE, related_name='ilustracionGenero')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, related_name='genero')
