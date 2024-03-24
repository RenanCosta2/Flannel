
from rest_framework.viewsets import ModelViewSet 
from estacionamentos.models import Empresa, Estacionamento, Locacao
from estacionamentos.api.serializers import EmpresaSerializer, EstacionamentoSerializer, LocacaoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class EmpresaViewSet(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    @action(detail=True, methods=['GET'])
    def estacionamentos(self, request, pk=None):
        empresa = self.get_object()
        seriealizer = EstacionamentoSerializer(Estacionamento.objects.all(), many=True)
        return Response(seriealizer.data)
    


class EstacionamentoViewSet(ModelViewSet):
    queryset = Estacionamento.objects.all()
    serializer_class = EstacionamentoSerializer

class LocacaoViewSet(ModelViewSet):
    queryset = Locacao.objects.all()
    serializer_class = LocacaoSerializer