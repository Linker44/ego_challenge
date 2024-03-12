from rest_framework import viewsets, status
from auto.serializers import AutoSerializer, FichaSerializer, CaracteristicaSerializer, HeroSerializer, PrestacionSerializer
from auto.models import Auto, Ficha, Caracteristica, Prestacion, Hero
from django_filters.rest_framework import DjangoFilterBackend
from auto.filters import AutoFilter
from rest_framework.response import Response

# Create your views here.


class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AutoFilter

    def create(self, request, *args, **kwargs):
        ficha_data = request.data.pop('ficha', None)
        auto_serializer = self.get_serializer(data=request.data)
        auto_serializer.is_valid(raise_exception=True)
        auto = auto_serializer.save()

        if ficha_data:
            hero_data = ficha_data.pop('hero')
            caracteristicas_data = ficha_data.pop('caracteristicas')
            prestaciones_data = ficha_data.pop('prestaciones')

            hero_serializer = HeroSerializer(data=hero_data)
            hero_serializer.is_valid(raise_exception=True)
            hero = hero_serializer.save()

            ficha = Ficha.objects.create(hero=hero, auto=auto, **ficha_data)

            for caracteristica_data in caracteristicas_data:
                Caracteristica.objects.create(
                    ficha=ficha, **caracteristica_data)

            for prestacion_data in prestaciones_data:
                Prestacion.objects.create(ficha=ficha, **prestacion_data)

        headers = self.get_success_headers(auto_serializer.data)
        return Response(auto_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        ficha_data = request.data.pop('ficha', None)

        auto_serializer = self.get_serializer(instance, data=request.data)
        auto_serializer.is_valid(raise_exception=True)
        auto_serializer.save()

        if ficha_data:
            hero_data = ficha_data.pop('hero')
            caracteristicas_data = ficha_data.pop('caracteristicas')
            prestaciones_data = ficha_data.pop('prestaciones')

            hero_instance = instance.ficha.hero
            hero_serializer = HeroSerializer(hero_instance, data=hero_data)
            hero_serializer.is_valid(raise_exception=True)
            hero_serializer.save()

            for caracteristica_data in caracteristicas_data:
                caracteristica_id = caracteristica_data.get('id', None)
                if caracteristica_id:
                    caracteristica = Caracteristica.objects.get(
                        id=caracteristica_id, ficha=instance.ficha)
                    caracteristica_serializer = CaracteristicaSerializer(
                        caracteristica, data=caracteristica_data)
                else:
                    caracteristica_serializer = CaracteristicaSerializer(
                        data=caracteristica_data)
                caracteristica_serializer.is_valid(raise_exception=True)
                caracteristica_serializer.save()

            for prestacion_data in prestaciones_data:
                prestacion_id = prestacion_data.get('id', None)
                if prestacion_id:
                    prestacion = Prestacion.objects.get(
                        id=prestacion_id, ficha=instance.ficha)
                    prestacion_serializer = PrestacionSerializer(
                        prestacion, data=prestacion_data)
                else:
                    prestacion_serializer = PrestacionSerializer(
                        data=prestacion_data)
                prestacion_serializer.is_valid(raise_exception=True)
                prestacion_serializer.save()

        return Response(auto_serializer.data)


class FichaViewSet(viewsets.ModelViewSet):
    queryset = Ficha.objects.all()
    serializer_class = FichaSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        hero_data = request.data.pop('hero')
        caracteristicas_data = request.data.pop('caracteristicas', [])
        prestaciones_data = request.data.pop('prestaciones', [])

        ficha_serializer = self.get_serializer(data=request.data)
        ficha_serializer.is_valid(raise_exception=True)

        hero_serializer = HeroSerializer(data=hero_data)
        hero_serializer.is_valid(raise_exception=True)
        hero = hero_serializer.save()

        ficha = ficha_serializer.save(hero=hero)

        for caracteristica_data in caracteristicas_data:
            caracteristica_data['ficha'] = ficha.id
            caracteristica_serializer = CaracteristicaSerializer(
                data=caracteristica_data)
            caracteristica_serializer.is_valid(raise_exception=True)
            caracteristica_serializer.save(ficha=ficha)

        for prestacion_data in prestaciones_data:
            prestacion_data['ficha'] = ficha.id
            prestacion_serializer = PrestacionSerializer(data=prestacion_data)
            prestacion_serializer.is_valid(raise_exception=True)
            prestacion_serializer.save(ficha=ficha)

        headers = self.get_success_headers(ficha_serializer.data)
        return Response(ficha_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        hero_data = request.data.pop('hero', None)
        caracteristicas_data = request.data.pop('caracteristicas', [])
        prestaciones_data = request.data.pop('prestaciones', [])

        if hero_data:
            hero_instance = instance.hero
            hero_serializer = HeroSerializer(hero_instance, data=hero_data)
            hero_serializer.is_valid(raise_exception=True)
            hero_serializer.save()

        ficha_serializer = self.get_serializer(instance, data=request.data)
        ficha_serializer.is_valid(raise_exception=True)
        ficha = ficha_serializer.save()

        for caracteristica_data in caracteristicas_data:
            caracteristica_id = caracteristica_data.get('id')
            if caracteristica_id:
                caracteristica_instance = Caracteristica.objects.get(
                    id=caracteristica_id, ficha=instance)
                caracteristica_serializer = CaracteristicaSerializer(
                    caracteristica_instance, data=caracteristica_data)
            else:
                caracteristica_serializer = CaracteristicaSerializer(
                    data=caracteristica_data)
            caracteristica_serializer.is_valid(raise_exception=True)
            caracteristica_serializer.save(ficha=ficha)

        for prestacion_data in prestaciones_data:
            prestacion_id = prestacion_data.get('id')
            if prestacion_id:
                prestacion_instance = Prestacion.objects.get(
                    id=prestacion_id, ficha=instance)
                prestacion_serializer = PrestacionSerializer(
                    prestacion_instance, data=prestacion_data)
            else:
                prestacion_serializer = PrestacionSerializer(
                    data=prestacion_data)
            prestacion_serializer.is_valid(raise_exception=True)
            prestacion_serializer.save(ficha=ficha)

        return Response(ficha_serializer.data)
