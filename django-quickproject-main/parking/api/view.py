from rest_framework.viewsets import ModelViewSet
from parking.models import Parking
from parking.api.serializers import ParkingSerializer

class ParkingCreateView(ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer

