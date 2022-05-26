from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Ps4Formulario(forms.Form):
    nombre= forms.CharField(max_length=30)
    genero= forms.CharField(max_length=30)
    precio= forms.FloatField()


class XboxFormulario(forms.Form):
    nombre= forms.CharField()
    genero= forms.CharField()
    precio= forms.FloatField()

class ColeccionFormulario(forms.Form):
    nombre= forms.CharField()
    genero= forms.CharField()
    consola= forms.CharField()


class PagoFormulario(forms.Form):
    metodo= forms.CharField()
    consola= forms.CharField()
    precio= forms.FloatField()

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la contraseña", widget= forms.PasswordInput)
    last_name= forms.CharField()
    first_name= forms.CharField()
    class Meta:
        model = User
        fields= ["username", "email", "password1", "password2", "last_name", "first_name"]
        help_texts= {k:"" for k in fields}


