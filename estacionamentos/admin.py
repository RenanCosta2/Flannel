from django.contrib import admin
from .models import Empresa , Estacionamento, Locacao


admin.site.register(Empresa)
admin.site.register(Estacionamento)
admin.site.register(Locacao)