from django.contrib import admin
from .models import Empresa , Estacionamento, VeiculoEstacionado, Historico


admin.site.register(Empresa)
admin.site.register(Estacionamento)
admin.site.register(VeiculoEstacionado)
admin.site.register(Historico)