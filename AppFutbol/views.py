from django.shortcuts import render
from .models import Jugador, Partidos, Equipo
from .forms import FormularioJugador, FormularioPartidos,FormularioEquipo
# Create your views here.

#Creo las views o controladores que van a contestar a las solicitudes del usuario

def inicio(request):
    return render(request, "index.html")

def jugadores(request):

    if request.method == 'POST':
        formulario = FormularioJugador(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            jugador = Jugador(nombre=informacion['nombre'], numero=informacion['numero'], posicion=informacion['posicion'],
                                 equipo=informacion['equipo'], edad=informacion['edad'])
            jugador.save()
            return render(request, "jugadores.html", {"mensaje":"Jugador Guardado Correctamente"})
        else:
            return render(request, "jugadores.html", {"mensaje":"Error al guardar el jugador"})
    #creo una instancia de la clase formulario
    formulario = FormularioJugador() 
    #se la envio al template para que renderise 
    return render(request, "jugadores.html", {"formulario":formulario })

def partidos(request):

    if request.method =='POST':
        formulario = FormularioPartidos(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            partido = Partidos(identificador=informacion['id_partido'], equipo1=informacion['equipo1'], equipo2=informacion['equipo2'],fechaPartido=informacion['fecha_partido'] )
            partido.save()
            return render(request, "partidos.html", {"mensaje":"Partido Guardado Correctamente"})
        else:
            return render(request, "partidos.html", {"mensaje":"Error al guardar el Partido"})
    formulario = FormularioPartidos() 
    return render(request, "partidos.html",  {"formulario":formulario })

def equipos(request):
    if request.method =='POST':
        formulario = FormularioEquipo(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            equipo = Equipo(nombre = informacion['nombre'], pais=informacion['pais'], nombreEntrenador=informacion['nombre_entrenador'])
            equipo.save()
            
            return render(request, "partidos.html", {"mensaje":"Entrenador Guardado Correctamente"})
        else:
            return render(request, "partidos.html", {"mensaje":"Error al guardar el Entrenador"})
    formulario = FormularioEquipo()   
    return render(request, "equipos.html",  {"formulario":formulario })

def BuscarJugadores(request):  
        return render(request, "BuscarJugador.html")

def Buscar(request):
        if request.method =='GET':
            if request.GET['nombre']:
                NombreJugador = request.GET['nombre']
                jugador = Jugador.objects.filter(nombre__icontains=NombreJugador)
                return render(request, "BuscarJugador.html", {"jugadores":jugador})   
            else:
                return render(request, "BuscarJugador.html",{"mensaje":"Debe ingresar el nombre del jugador"})

def VerEquipos(request):
        equipos = Equipo.objects.all()
        return render(request, "VerEquipos.html", {"equipos":equipos})   

def VerPartidos(request):
        partidos = Partidos.objects.all()
        return render(request, "VerPartidos.html", {"partidos":partidos})   
