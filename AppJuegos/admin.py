from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(PS4)
admin.site.register(Xbox)
admin.site.register(Coleccion)
admin.site.register(Pago)
