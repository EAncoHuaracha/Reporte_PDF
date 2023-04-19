from django.db import models

# Create your models here.

class Parasito(models.Model):
    nombre = models.CharField(max_length=30)
    departamento = models.CharField(max_length=30)
    prevalencia = models.IntegerField()

    def __str__(self):
        return self.nombre