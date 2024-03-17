from rest_framework.viewsets import ModelViewSet 
from estacionamentos.models import Empresa
from estacionamentos.api.serializers import EmpresaSerializer

class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    
  
