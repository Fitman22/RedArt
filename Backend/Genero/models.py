from django.db import models

class Genero(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField(default='')


