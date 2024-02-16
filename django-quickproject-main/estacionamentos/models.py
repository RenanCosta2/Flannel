from django.db import models
from users.models import Empresa, Gerente, Funcionario

class Endereco(models.Model):
    rua = models.CharField(max_length=100, default='')
    numero = models.CharField(max_length=100, default='')
    cidade = models.CharField(max_length=50, default='')
    estado = models.CharField(max_length=50, default='')
    bairro = models.CharField(max_length=100, default='')
    cep = models.CharField(max_length=8, default='')
    
    def __str__(self):
        return self.rua

class Estacionamento(models.Model):
    idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE) # Não sei como isso funcionaaaa
    idEmpresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    idGerente = models.ForeignKey(Gerente, on_delete=models.CASCADE)
    idfuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE) # Aqui serão mais de um funcionário, mas n sei como colocar ainda

    def __str__(self):
        return self.idGerente
    