from django.urls import path
from AppJuegos import views


urlpatterns = [
    path("", views.inicio, name= "Inicio"),
    path("xbox", views.juegosXbox, name= "Xbox"),
    path("ps4", views.juegosPS4, name= "PS4"),
    path("colecciones", views.colecciones, name= "Colecciones"),
    path("pagos", views.pagos, name= "Pagos"),
    path("juegosPS4Formulario", views.ps4formulario, name=" JuegosPS4Formulario"),
    path("juegosXboxFormulario", views.xboxformulario, name= "JuegosXboxFormulario"),
    path("pagoFormulario", views.pagoformulario, name=" PagoFormulario"),
    path("coleccionFormulario", views.coleccionformulario, name=" ColeccionFormulario"),
    path("busquedaGeneroPs4", views.busquedaGeneroPs4, name= "BusquedaGeneroPs4"),
    path("buscar/", views.buscar),
    ]