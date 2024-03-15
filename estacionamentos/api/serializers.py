from rest_framework import serializers
from estacionamentos.models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Empresa
        fields = ['id', 'nome', 'cnpj', 'email', 'plano']