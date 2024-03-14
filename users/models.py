from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GerenteGeral(models.Model):

    nome = models.CharField(max_length=100, verbose_name='Nome completo', blank=False, null=False, unique=False)
    cpf = models.CharField(max_length=11, verbose_name='Cadastro de Pessoa Física', blank=False, null=False, unique=True)
    telefone = models.CharField(max_length=11, verbose_name='Telefone', null=False, unique=True, blank=False)
    email = models.CharField(max_length=100, verbose_name='E-mail', blank=False, null=False, unique=True)
    senha = models.CharField(max_length=50, verbose_name='Senha', blank=False, null=False, unique=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Gerente Geral"
        verbose_name_plural = "Gerentes Gerais"

class GerenteLocal(models.Model):

    nome = models.CharField(max_length=100, verbose_name='Nome completo', blank=False, null=False, unique=False)
    cpf = models.CharField(max_length=11, verbose_name='Cadastro de Pessoa Física', blank=False, null=False, unique=True)
    telefone = models.CharField(max_length=11, verbose_name='Telefone', null=False, unique=True, blank=False)
    email = models.CharField(max_length=100, verbose_name='E-mail', blank=False, null=False, unique=True)
    senha = models.CharField(max_length=50, verbose_name='Senha', blank=False, null=False, unique=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Gerente Local"
        verbose_name_plural = "Gerentes Locais"
