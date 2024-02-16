from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Empresa(models.Model):

    nome = models.CharField(max_length=100, default=' ')
    email = models.CharField(max_length=150)
    telefone = models.CharField(max_length=12)
    cnpj = models.CharField(max_length=14, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
 
class Gerente(models.Model): # O ideal aqui seria que Gerente hedasse de funcionario, mas n sei como fazer isso

    nome = models.CharField(max_length=100, default=' ')
    email = models.CharField(max_length=150)
    telefone = models.CharField(max_length=12)
    cpf = models.CharField(max_length=14, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
 
class Funcionario(models.Model):

    nome = models.CharField(max_length=100, default=' ')
    email = models.CharField(max_length=150)
    telefone = models.CharField(max_length=12)
    cpf = models.CharField(max_length=14, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
 