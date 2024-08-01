from django.db import models
from Usuario.models import Usuario

class Seguido (models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuarioSeguido')
    userName = models.CharField(max_length=50)
