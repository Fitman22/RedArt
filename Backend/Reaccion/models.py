from django.db import models
from Ilustracion.models import Ilustracion
from Usuario.models import Usuario

class Reaccion(models.Model):
    ilustracion = models.ForeignKey(Ilustracion, on_delete= models.CASCADE, related_name='ilustracionReaccion')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuarioReaccion')
    like = models.CharField(max_length= 50)
    love = models.CharField(max_length=50)
    funny = models.CharField(max_length=50)
    sad = models.CharField(max_length=50)
