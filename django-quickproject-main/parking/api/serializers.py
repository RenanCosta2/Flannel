from rest_framework import serializers
from parking.models import Parking

class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ['company', 'local', 'carCapacity']