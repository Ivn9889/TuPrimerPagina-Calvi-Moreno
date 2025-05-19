from django.db import models

# Create your models here.

class Pelicula (models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=10)
    sinopsis = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} - {self.genero}"
class Serie (models.Model):
    nombre = models.CharField(max_length=40)
    genero = models.CharField(max_length=10)
    sinopsis = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre} - {self.genero}"
class Opinion (models.Model):
    critica = models.CharField(max_length=100)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, null=True, blank=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.critica}"

