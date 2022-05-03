from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import is_valid_path
import AppJuegos
from AppJuegos.forms import Ps4Formulario, XboxFormulario, ColeccionFormulario, PagoFormulario
from AppJuegos.models import PS4, Xbox, Coleccion, Pago
# Create your views here.

def inicio(request):
    
    return render(request, "AppJuegos/inicio.html")

def juegosPS4(request):
    if request.method == "POST":
        miFormulario = Ps4Formulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            ps4= PS4(nombre=informacion["nombre"], genero=informacion["genero"], precio=informacion["precio"])
            ps4.save()
            return render(request, "AppJuegos/inicio.html")

    else:
        miFormulario = Ps4Formulario()
    return render(request, "AppJuegos/juegosPS4.html", {"miFormulario": miFormulario})

def juegosXbox(request):
    return render(request, "AppJuegos/juegosXbox.html")

def colecciones(request):
    return render(request, "AppJuegos/colecciones.html")

def pagos(request):
    return render(request, "AppJuegos/pagos.html")

def ps4formulario(request):
    #if request.method == "POST":
     #   miFormulario = Ps4Formulario(request.POST)
      #  print(miFormulario)
       # if miFormulario.is_valid():
        #    informacion= miFormulario.cleaned_data
         #   ps4= PS4(nombre=informacion["nombre"], genero=informacion["genero"], precio=informacion["precio"])
          #  ps4.save()
           # return render(request, "AppJuegos/inicio.html")

    #else:
     #   miFormulario = Ps4Formulario()
    #return render(request, "AppJuegos/juegosPS4Formulario.html", {"miFormulario": miFormulario})
    return
def xboxformulario(request):
    if request.method == "POST":
        miFormulario= XboxFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            xbox= Xbox(nombre=informacion["nombre"], genero=informacion["genero"], precio=informacion["precio"])
            xbox.save()
            return render(request, "AppJuegos/inicio.html")

    else:
        miFormulario = XboxFormulario()
    return render(request, "AppJuegos/juegosXboxFormulario.html", {"miFormulario": miFormulario})

def coleccionformulario(request):
    if request.method == "POST":
        miFormulario= ColeccionFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            colec= Coleccion(nombre=informacion["nombre"], genero=informacion["genero"], consola=informacion["consola"])
            colec.save()
            return render(request, "AppJuegos/inicio.html")

    else:
        miFormulario = ColeccionFormulario()
    return render(request, "AppJuegos/coleccionFormulario.html", {"miFormulario": miFormulario})

def pagoformulario(request):
    if request.method == "POST":
        miFormulario= PagoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            pago= Coleccion(nombre=informacion["nombre"], genero=informacion["genero"], consola=informacion["consola"])
            pago.save()
            return render(request, "AppJuegos/inicio.html")

    else:
        miFormulario = PagoFormulario()
    return render(request, "AppJuegos/pagoFormulario.html", {"miFormulario": miFormulario})

def busquedaGeneroPs4(request):
    return render(request, "AppJuegos/busquedaGeneroPs4.html")

def buscar(request):
    
    if request.GET["genero"]:
        genero= request.GET['genero']
        juegosps4= PS4.objects.filter(genero__iexact=genero)
        return render(request, "AppJuegos/resultadoBusqueda.html", {"juegosps4": juegosps4, "genero": genero})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)


    