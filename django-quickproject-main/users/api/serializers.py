from rest_framework import serializers
from users.models import  Empresa, Gerente, Funcionario
 
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['id', 'address', 'phone_number', 'birth_date', 'user']
 
class GerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        fields = ['id', 'address', 'phone_number', 'birth_date', 'user']
 
class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ['id', 'address', 'phone_number', 'birth_date', 'user']
  