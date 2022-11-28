from django.db import models

# Create your models here.

#creo el modelo jugador
#con sus respectivas propiedades

class Jugador(models.Model):
    nombre = models.CharField(max_length=20)
    numero = models.IntegerField()
    posicion = models.CharField(max_length=10)
    equipo = models.CharField(max_length=20)
    edad = models.IntegerField()

class Equipo(models.Model):
    nombre = models.CharField(max_length=20)
    pais = models.CharField(max_length=10)
    nombreEntrenador = models.CharField(max_length=20)

class Partidos(models.Model):
    ide = models.IntegerField()
    equipo1 = models.CharField(max_length=20)
    equipo2 = models.CharField(max_length=20)
    fechaPartido = models.DateField()