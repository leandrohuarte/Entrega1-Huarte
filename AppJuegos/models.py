from django.db import models

# Create your models here.
class PS4 (models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    precio = models.FloatField()
    class Meta:
        verbose_name= "Ps4"
        verbose_name_plural= "Ps4"
    def __str__(self):
        txt = "{0} - {1} - {2}"
        return txt.format(self.nombre, self.genero, self.precio)

class Xbox (models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    precio = models.FloatField()
    class Meta:
        verbose_name= "Xbox"
        verbose_name_plural= "Xbox"
    def __str__(self):
        txt = "{0} - {1} - {2}"
        return txt.format(self.genero, self.nombre, self.precio)

class Coleccion (models.Model):
    nombre = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    consola = models.CharField(max_length=50)
    class Meta:
        verbose_name= "Coleccion"
        verbose_name_plural= "Colecciones"
    def __str__(self):
        txt = "{0} - {1} - {2}"
        return txt.format(self.genero, self.nombre, self.consola)

class Pago (models.Model):  #no sé si es mejor poner pago o explicacion, y lo de variables si se te ocurre algo mejor joya
    metodo = models.CharField(max_length=50)   #tarjeta, transferencia, mercadopago, efectivo
    consola = models.CharField(max_length=50)  
    precio = models.FloatField()  #lo que va a pagar
    def __str__(self):
        txt = "{0} - {1} - {2} "
        return txt.format(self.metodo, self.consola, self.precio)