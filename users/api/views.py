from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import GerenteGeralSerializer, GerenteLocalSerializer

from users.models import GerenteGeral, GerenteLocal

class GerenteGeralViewSet(ModelViewSet):
    serializer_class = GerenteGeralSerializer
    permission_classes = [AllowAny]
    queryset = GerenteGeral.objects.all()
    http_method_names = ['get', 'put']

class GerenteLocalViewSet(ModelViewSet):
    serializer_class = GerenteLocalSerializer
    permission_classes = [AllowAny]
    queryset = GerenteLocal.objects.all()
    http_method_names = ['get', 'put']
