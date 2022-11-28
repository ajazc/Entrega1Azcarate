
from django.urls import path
from AppFutbol.views import *


#Estas son las rutas
urlpatterns = [
    path("", inicio, name="inicio"),
    path("jugadores/", jugadores, name="jugadores"),
    path("equipos/", equipos, name="equipos"),
    path("partidos/", partidos, name="partidos"),

    

]