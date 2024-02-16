from django.contrib import admin
from users.models import Empresa, Gerente, Funcionario

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Gerente)
admin.site.register(Funcionario)