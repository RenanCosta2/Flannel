from django.db import models

class Estacionamento(models.Model):
    nome = models.CharField(max_length=100) # para teste
    idEmpresa = models.IntegerField()
    idEndereco = models.IntegerField()
    idGerente = models.IntegerField()
    idfuncionario = models.IntegerField() # Aqui tenho que trocar para array

    def __str__(self):
        return self.nome
    
class Endereco(models.Model):
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    
    def __str__(self):
        return self.rua