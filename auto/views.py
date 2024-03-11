from rest_framework import viewsets
from auto.serializers import AutoSerializer, FichaSerializer, CaracteristicaSerializer
from auto.models import Auto, Ficha, Caracteristica
from django_filters.rest_framework import DjangoFilterBackend
from auto.filters import AutoFilter

# Create your views here.


class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AutoFilter


class FichaViewSet(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer


class CaracteristicaViewSet(viewsets.ModelViewSet):
    queryset = Caracteristica.objects.all()
    serializer_class = CaracteristicaSerializer
