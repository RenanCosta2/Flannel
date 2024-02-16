from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import UserProfileExampleSerializer, EmpresaSerializer, GerenteSerializer, FuncionarioSerializer

from users.models import UserProfileExample, Empresa, Gerente, Funcionario

class UserProfileExampleViewSet(ModelViewSet):
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']
 
class EmpresaViewSet(ModelViewSet):
    serializer_class = EmpresaSerializer
    permission_classes = [AllowAny]
    queryset = Empresa.objects.all()
    http_method_names = ['get', 'put']
 
class GerenteViewSet(ModelViewSet):
    serializer_class = GerenteSerializer
    permission_classes = [AllowAny]
    queryset = Gerente.objects.all()
    http_method_names = ['get', 'put']
 
class FuncionarioViewSet(ModelViewSet):
    serializer_class = FuncionarioSerializer
    permission_classes = [AllowAny]
    queryset = Funcionario.objects.all()
    http_method_names = ['get', 'put']
 