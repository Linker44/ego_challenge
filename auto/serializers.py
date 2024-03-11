from rest_framework import serializers
from auto.models import Auto, Ficha, Caracteristica


class CaracteristicaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Caracteristica
        fields = '__all__'


class FichaSerializer(serializers.HyperlinkedModelSerializer):
    caracteristicas = CaracteristicaSerializer(many=True, read_only=True)

    class Meta:
        model = Ficha
        fields = '__all__'


class AutoSerializer(serializers.HyperlinkedModelSerializer):

    ficha = FichaSerializer(many=False, read_only=True)

    class Meta:
        model = Auto
        fields = '__all__'
