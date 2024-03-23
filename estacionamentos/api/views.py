from rest_framework.viewsets import ModelViewSet 
from estacionamentos.models import Empresa, Estacionamento, Locacao
from estacionamentos.api.serializers import EmpresaSerializer, EstacionamentoSerializer, LocacaoSerializer

class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EstacionamentoViewSet(ModelViewSet):
    queryset = Estacionamento.objects.all()
    serializer_class = EstacionamentoSerializer

class LocacaoViewSet(ModelViewSet):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer