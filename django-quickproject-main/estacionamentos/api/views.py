from rest_framework.viewsets import ModelViewSet
from estacionamentos.models import Estacionamento, Endereco
from estacionamentos.api.serializers import EstacionamentoSerializer, EnderecoSerializer

class EstacionamentoListCreateView(ModelViewSet):
    queryset = Estacionamento.objects.all()
    serializer_class = EstacionamentoSerializer

class EnderecoListCreateView(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer