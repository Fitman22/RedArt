from django.db import models
from Usuario.models import Usuario

class Seguidor (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuarioSeguidor')
    userName = models.CharField(max_length=50)
    