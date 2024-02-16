from rest_framework import serializers
from estacionamentos.models import Estacionamento, Endereco

class EstacionamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estacionamento
        fields = ['nome', 'idEmpresa', 'idEndereco', 'idGerente', 'idfuncionario']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'cidade', 'estado', 'bairro', 'cep']