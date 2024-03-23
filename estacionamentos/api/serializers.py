from rest_framework import serializers
from estacionamentos.models import Empresa, Estacionamento, Locacao

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Empresa
        fields = ['id', 'nome', 'cnpj', 'email', 'plano']

class EstacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamento
        fields = ['id', 'idEmpresa', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'capacidade', 'lotacao']

class LocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locacao
        fields = ['id', 'idEstacionamento', 'dataEntrada', 'dataSaida', 'valor', 'placaCarro', 'flannerPrime']