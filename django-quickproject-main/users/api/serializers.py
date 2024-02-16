from rest_framework import serializers
from users.models import  Empresa, Gerente, Funcionario
 
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'nome', 'email', 'telefone', 'cnpj', "plano", 'user']
 
class GerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        fields = ['id', 'nome', 'email', 'telefone','cpf', 'user']

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'email', 'telefone','cpf', 'user']
  