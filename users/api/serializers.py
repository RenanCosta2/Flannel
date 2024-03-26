from rest_framework import serializers
from users.models import GerenteGeral, GerenteLocal

class GerenteGeralSerializer(serializers.ModelSerializer):

    class Meta:
        model = GerenteGeral
        fields = ['id', 'nome', 'cpf', 'telefone', 'email', 'senha', 'user']
        extra_kwargs = {
            'senha': {'write_only': True}
        }


class GerenteLocalSerializer(serializers.ModelSerializer):

    class Meta:
        model = GerenteLocal
        fields = ['id', 'nome', 'cpf', 'telefone', 'email', 'senha', 'user']
        
        extra_kwargs = {
            'senha': {'write_only': True}
        }