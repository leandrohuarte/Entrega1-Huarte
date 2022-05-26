from msilib.schema import ListView
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import is_valid_path
import AppJuegos
from AppJuegos.forms import Ps4Formulario, UserRegisterForm, UserCreationForm , XboxFormulario, ColeccionFormulario, PagoFormulario
from AppJuegos.models import PS4, Xbox, Coleccion, Pago
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.


def inicio(request):
    
    return render(request, "AppJuegos/inicio.html")

def juegosPS4(request):
    if request.method == "POST":
        miFormulario = Ps4Formulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            ps4= PS4(nombre=informacion["nombre"], genero=informacion["genero"], precio=informacion["precio"])
            ps4.save()
            return render(request, "AppJuegos/inicio.html")

    else:
        miFormulario = Ps4Formulario()
    return render(request, "AppJuegos/juegosPS4.html", {"miFormulario": miFormulario})

@login_required
def juegosXbox(request):
    if request.method == "POST":
        miFormulario = XboxFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            xbox= Xbox(nombre=informacion["nombre"], genero=informacion["genero"], precio=informacion["precio"])
            xbox.save()
            return render(request, "AppJuegos/inicio.html")

    else:
        miFormulario = XboxFormulario()
    return render(request, "AppJuegos/juegosXbox.html", {"miFormulario": miFormulario})
    
    #return render(request, "AppJuegos/juegosXbox.html")

def colecciones(request):
    return render(request, "AppJuegos/colecciones.html")

def pagos(request):
    if request.method == "POST":
        miFormulario = PagoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            pago= Pago(metodo=informacion["metodo"], consola=informacion["consola"], precio=informacion["precio"])
            pago.save()
            return render(request, "AppJuegos/inicio.html")

    else:
        miFormulario = PagoFormulario()
        return render(request, "AppJuegos/pagos.html", {"miFormulario": miFormulario})

    #return render(request, "AppJuegos/pagos.html")

def ps4formulario(request):
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
    return render(request, "AppJuegos/juegosPS4Formulario.html", {"miFormulario": miFormulario})

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
        genero= request.GET["genero"]
        juegosps4= PS4.objects.filter(genero__iexact=genero)
        return render(request, "AppJuegos/resultadoBusqueda.html", {"juegosps4": juegosps4, "genero": genero})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

@login_required
def leerJuegosps4(request):
    juegosps4 = PS4.objects.all
    contexto= {"juegosps4":juegosps4}
    return render(request, "AppJuegos/leerjuegosps4.html", contexto)

def eliminarJuegops4(request, juegosps4_nombre):
    juegosps4= PS4.objects.get(nombre=juegosps4_nombre)
    juegosps4.delete()
    juegossps4= PS4.objects.all()
    contexto= {"juegosps4":juegossps4}
    return render(request, "AppJuegos/leerJuegosps4.html", contexto)
 
def editarJuegosps4(request, juegosps4_nombre):
    juegosps4= PS4.objects.get(nombre=juegosps4_nombre)
    if request.method == 'POST':
        miFormulario =  Ps4Formulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion= miFormulario.cleaned_data
            juegosps4.nombre = informacion ['nombre']
            juegosps4.genero = informacion ['genero']
            juegosps4.precio = informacion ['precio']
            juegosps4.save()
            return render(request, "AppJuegos/inicio.html")
    else:
        miFormulario = Ps4Formulario(initial={'nombre': juegosps4.nombre, 'genero': juegosps4.genero, 'precio': juegosps4.precio})
    return render(request, "AppJuegos/editarJuegosps4.html", {"miFormulario": miFormulario, "juegosps4_nombre": juegosps4_nombre})

class JuegosXboxList(LoginRequiredMixin, ListView):
    model = Xbox
    template_name = "AppJuegos/listaJuegosXbox.html"

class JuegosXboxDetalle(DetailView):
    model = Xbox
    template_name = "AppJuegos/juegosXboxDetalle.html"

class JuegosXboxCreacion(CreateView):
    model = Xbox
    success_url = "/AppJuegos/xbox/listaJuegosXbox"
    fields = ["nombre", "genero", "precio"]

class JuegosXboxUpdate(UpdateView):
    model = Xbox
    success_url = "/AppJuegos/xbox/listaJuegosXbox"
    fields = ["nombre", "genero", "precio"]

class JuegosXboxDelete(DeleteView):
    model = Xbox
    success_url = "/AppJuegos/xbox/listaJuegosXbox"

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contra=form.cleaned_data.get('password')
            user= authenticate(username=usuario, password=contra)
            if user:
                login(request, user)
                return render(request, "AppJuegos/inicio.html", {'mensaje':f"Bienvenid@ {user}!"})
        else:
            return render(request, "AppJuegos/inicio.html", {'mensaje':"Error. Datos incorrectos"})
    else:
        form = AuthenticationForm()
    return render(request, "AppJuegos/login.html", {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            return render(request, "AppJuegos/inicio.html", {"mensaje":"Usuario creado :)"})
    else:
        form=UserRegisterForm()
    return render(request, "AppJuegos/registro.html", {"form": form})

def editarUsuario(request):
    usuario= request.user
    if request.method == "POST":
        miFormulario= UserRegisterForm(request.POST)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            usuario.username=informacion["username"]
            usuario.email= informacion["email"]
            usuario.password1= informacion["password1"]
            usuario.password2= informacion["password2"]
            usuario.save()

            return render(request, "AppJuegos/inicio.html")
    else:
        miFormulario= UserRegisterForm(initial={"username": usuario.username, "email": usuario.email})
    return render(request, "AppJuegos/editarPerfil.html",{'miFormulario': miFormulario, 'usuario': usuario.username})