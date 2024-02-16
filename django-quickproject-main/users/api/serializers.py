from rest_framework import serializers
from users.models import UserProfileExample, Empresa, Gerente, Funcionario

class UserProfileExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileExample
        fields = ['id', 'address', 'phone_number', 'birth_date', 'user']
 
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
  