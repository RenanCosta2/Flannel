from django.db import models
from users.models import Empresa, Gerente, Funcionario

class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=8)
    
    def __str__(self):
        return self.rua

class Estacionamento(models.Model):
    # idEndereco = models.ForeignKey(Endereco) # Não sei como isso funcionaaaa
    # idEmpresa = models.ForeignKey(Empresa)
    # idGerente = models.ForeignKey(Gerente)
    # idfuncionario = models.ForeignKey(Funcionario) # Aqui serão mais de um funcionário, mas n sei como colocar ainda

    def __str__(self):
        return self.idGerente
    