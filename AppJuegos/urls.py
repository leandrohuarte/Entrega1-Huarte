from django.urls import path, re_path
from AppJuegos import views
from django.contrib.auth.views import LogoutView


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
    path("leerjuegosps4", views.leerJuegosps4, name= "LeerJuegosPs4"),
    path("eliminarJuegops4/<juegosps4_nombre>", views.eliminarJuegops4, name="EliminarJuegosPs4"),
    path("editarJuegosps4/<juegosps4_nombre>", views.editarJuegosps4, name= "EditarJuegosPs4" ),
    path("xbox/listajuegosxbox/", views.JuegosXboxList.as_view(), name= "ListaJuegosXbox"),
    path(r'^(?P<pk>\d+)$', views.JuegosXboxDetalle.as_view(), name="Detail"),
    #path(r'nuevo$', views.JuegosXboxCreacion.as_view(), name ="New"),
    #path(r'^editar/(?P<pk>\d+)$', views.JuegosXboxUpdate.as_view(), name= "Edit"),
    #path(r'^borrar/(?P<pk>\d+)$', views.JuegosXboxDelete.as_view(), name= "Delete"),
    path(r'juego_nuevo', views.JuegosXboxCreacion.as_view(), name ="New"),
    path(r'editar_juego/<pk>', views.JuegosXboxUpdate.as_view(), name= "Edit"),
    path(r'borrar_juego/<pk>', views.JuegosXboxDelete.as_view(), name= "Delete"),
    path("login", views.login_request, name = "Login"),
    path("register", views.register, name= "Register"),
    path("logout", LogoutView.as_view(template_name="AppJuegos/logout.html"), name= "Logout"),
    path("editarPerfil", views.editarUsuario, name="EditarPerfil"), 
    path("acercanuestro", views.acerca, name= "about"),


    
    ]