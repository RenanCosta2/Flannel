from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(verbose_name="Nome da empresa", max_length=100, unique=True, null=False, blank=False)
    cnpj = models.CharField(verbose_name="CNPJ da empresa", max_length=14, unique=True, null=False, blank=False)
    email = models.CharField(verbose_name="Email da empresa", max_length=100, unique=True, null=False, blank=False)
    plano = models.IntegerField(verbose_name="Plano de assinatura", default=0)

    def __str__(self):
        return self.nome

# Deixei tudo comentado
# class Estacionamento(models.Model):
#     idEmpresa = models.ForeignKey(Empresa, verbose_name="Id da empresa proprietária do estacionamento", on_delete=models.CASCADE)
#     rua = models.CharField(verbose_name="Nome da rua do estacionamento", max_length=100, null=False, blank=False)
#     numero = models.CharField(verbose_name="Número do estacionamento", max_length=10, null=False, blank=False)
#     bairro = models.CharField(verbose_name="Nome do bairro", max_length=50, null=False, blank=False)
#     cidade = models.CharField(verbose_name="Nome da cidade", max_length=50, null=False, blank=False)
#     estado = models.CharField(verbose_name="UF do estado", max_length=2, null=False, blank=False)
#     capacidade = models.IntegerField(verbose_name="Capacidade de veiculos do estacionamento", null=False, blank=False)
#     lotacao = models.IntegerField(verbose_name="Número veiculos no estacionamento", default=0)

#     def __str__(self):
#         return self.idEmpresa.cnpj