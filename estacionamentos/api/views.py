from rest_framework.viewsets import ModelViewSet 
from estacionamentos.models import Empresa, Estacionamento, VeiculoEstacionado, Historico
from estacionamentos.api.serializers import EmpresaSerializer, EstacionamentoSerializer, VeiculoEstacionadoSerializer, HistoricoSerializer

class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EstacionamentoViewSet(ModelViewSet):
    queryset = Estacionamento.objects.all()
    serializer_class = EstacionamentoSerializer

class VeiculoEstacionadoViewSet(ModelViewSet):
    queryset = VeiculoEstacionado.objects.all()
    serializer_class = VeiculoEstacionadoSerializer

class HistoricoViewSet(ModelViewSet):
    queryset = Historico.objects.all()
    serializer_class = HistoricoSerializer
