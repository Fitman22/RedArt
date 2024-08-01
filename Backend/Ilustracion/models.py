from django.db import models

class Ilustracion(models.Model):
    Description = models.CharField(max_length=500)
    Image = models.CharField(max_length=150)

