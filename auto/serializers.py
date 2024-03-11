from rest_framework import serializers
from auto.models import Auto, Ficha, Caracteristicas


class CaracteristicasSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Caracteristicas
        fields = '__all__'


class FichaSerializer(serializers.HyperlinkedModelSerializer):
    caracteristicas = CaracteristicasSerializer(many=True, read_only=True)

    class Meta:
        model = Ficha
        fields = '__all__'


class AutoSerializer(serializers.HyperlinkedModelSerializer):

    ficha = FichaSerializer(many=False, read_only=True)

    class Meta:
        model = Auto
        fields = '__all__'
