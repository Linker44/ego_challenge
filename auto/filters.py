import django_filters
from auto.models import Auto


class AutoFilter(django_filters.FilterSet):
    fecha_auto_gt = django_filters.DateFilter(
        field_name='fecha_auto', lookup_expr='gte')
    fecha_auto_lt = django_filters.DateFilter(
        field_name='fecha_auto', lookup_expr='lte')
    precio_gt = django_filters.NumberFilter(
        field_name='precio', lookup_expr='gte')
    precio_lt = django_filters.NumberFilter(
        field_name='precio', lookup_expr='lte')

    class Meta:
        model = Auto
        fields = ['precio', 'fecha_auto', 'tipo']
