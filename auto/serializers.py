from rest_framework import serializers
from auto.models import Auto, Ficha, Caracteristica, Hero, Prestacion


class PrestacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prestacion
        fields = "__all__"


class HeroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hero
        fields = '__all__'


class CaracteristicaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Caracteristica
        fields = '__all__'


class FichaSerializer(serializers.HyperlinkedModelSerializer):
    hero = HeroSerializer(read_only=True)
    caracteristicas = CaracteristicaSerializer(many=True, read_only=True)
    prestaciones = PrestacionSerializer(many=True, read_only=True)

    class Meta:
        model = Ficha
        fields = '__all__'


class AutoSerializer(serializers.HyperlinkedModelSerializer):

    ficha = FichaSerializer(read_only=True)

    class Meta:
        model = Auto
        fields = '__all__'
