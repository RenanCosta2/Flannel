from django.contrib import admin
from estacionamentos.models import Estacionamento, Endereco

# Register your models here.

admin.site.register(Estacionamento)
admin.site.register(Endereco)