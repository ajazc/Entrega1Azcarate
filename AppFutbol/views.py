from django.shortcuts import render

# Create your views here.

#Creo las views o controladores que van a contestar a las solicitudes del usuario

def inicio(request):
    return render(request, "AppFutbol/inicio.html")
