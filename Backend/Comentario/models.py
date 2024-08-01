from django.db import models
from Ilustracion.models import Ilustracion
from Usuario.models import Usuario

class Comentario(models.Model):
    ilustracion = models.ForeignKey(Ilustracion, on_delete=models.CASCADE, related_name='ilustracionComentario')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuarioComentario')
    comment = models.TextField(default='')

