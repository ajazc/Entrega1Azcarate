from django import forms

# Aca voy a comenzar a crear los formularios


class FormularioJugador(forms.Form):
    nombre = forms.CharField(max_length=20)
    numero = forms.IntegerField()
    posicion = forms.CharField(max_length=10)
    equipo = forms.CharField(max_length=20)
    edad = forms.IntegerField()

class FormularioEquipo(forms.Form):
    nombre = forms.CharField(max_length=20)
    pais = forms.CharField(max_length=10)
    nombre_entrenador = forms.CharField(max_length=20)

class FormularioPartidos(forms.Form):
    id_partido = forms.IntegerField()
    equipo1 = forms.CharField(max_length=20)
    equipo2 = forms.CharField(max_length=20)
    fecha_partido = forms.DateField()