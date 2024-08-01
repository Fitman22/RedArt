from django.db import models
from Ilustracion.models import Ilustracion

class Usuario (models.Model):
    ilustracion = models.ForeignKey(Ilustracion, on_delete= models.CASCADE, related_name='ilustracionUsuario')
    name = models.CharField(max_length=50)
    lasName = models.CharField(max_length= 50)
    userName = models.CharField(max_length=50)
    description = models.TextField(default='')
    age = models.IntegerField(default=0)
    email = models.EmailField(default='')
    password = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    telephone = models.IntegerField(default=0)
