from django.shortcuts import render
from .models import Jugador, Partidos, Equipo
# Create your views here.

#Creo las views o controladores que van a contestar a las solicitudes del usuario

def inicio(request):
    return render(request, "index.html")

def jugadores(request):
    return render(request, "jugadores.html")

def partidos(request):
    return render(request, "partidos.html")

def equipos(request):
    return render(request, "equipos.html")