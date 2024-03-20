from rest_framework import serializers
from estacionamentos.models import Empresa, Estacionamento, VeiculoEstacionado, Historico

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Empresa
        fields = ['id', 'nome', 'cnpj', 'email', 'plano']

class EstacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamento
        fields = ['id', 'idEmpresa', 'rua', 'numero', 'bairro', 'cidade', 'estado', 'capacidade', 'lotacao']

class VeiculoEstacionadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VeiculoEstacionado
        fields = ['id', 'idEstacionamento', 'dataEntrada', 'placaCarro', 'cpf']

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historico
        fields = ['id', 'idEstacionamento', 'dataEntrada', 'dataSaida', 'placaCarro', 'cpf']