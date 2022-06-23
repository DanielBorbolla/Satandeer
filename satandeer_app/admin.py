from django.contrib import admin
from .models import Cliente, Tarjeta, ClienteTarjeta
# Register your models here.


class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "fechaNacimiento", "genero", "tipo")


class TarjetaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "descripcion", "interes")


class ClienteTarjetaAdmin(admin.ModelAdmin):
    list_display = ("numeroTarjeta", "cliente", "tarjeta", "creditoMax")


admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Tarjeta, TarjetaAdmin)
admin.site.register(ClienteTarjeta, ClienteTarjetaAdmin)
