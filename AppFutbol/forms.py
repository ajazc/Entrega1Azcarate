from django import forms

# Aca voy a comenzar a crear los formularios


class Jugador(forms.Form):
    nombre = forms.CharField(max_length=20)
    numero = forms.IntegerField()
    posicion = forms.CharField(max_length=10)
    equipo = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class Equipo(forms.Form):
    nombre = forms.CharField(max_length=20)
    pais = forms.CharField(max_length=10)
    nombreEntrenador = forms.CharField(max_length=20)

class Partidos(forms.Form):
    ide = forms.IntegerField()
    equipo1 = forms.CharField(max_length=20)
    equipo2 = forms.CharField(max_length=20)
    fechaPartido = forms.DateField()