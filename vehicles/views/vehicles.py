from rest_framework import viewsets

from ..models import Part, Vehicle
from ..serializers.vehicles import PartSerializer, VehicleSerializer


class PartViewSet(viewsets.ModelViewSet):
    serializer_class = PartSerializer
    queryset = Part.objects.all()   # A simper way to set queryset of a viewset


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        return Vehicle.objects.all()
