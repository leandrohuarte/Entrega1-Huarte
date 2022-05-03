from django import forms
class Ps4Formulario(forms.Form):
    nombre= forms.CharField()
    genero= forms.CharField()
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
