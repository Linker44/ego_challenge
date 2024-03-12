from django.contrib import admin
from auto.models import Auto, Ficha, Caracteristica, Hero, Prestacion

# Register your models here.


class CaracteristicaInline(admin.StackedInline):
    model = Caracteristica
    extra = 1


class PrestacionInline(admin.StackedInline):
    model = Prestacion
    extra = 1


class FichaAdmin(admin.ModelAdmin):
    fields = ["hero"]
    inlines = [CaracteristicaInline, PrestacionInline]


admin.site.register(Ficha, FichaAdmin)


@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'fecha_auto', 'precio')
    search_fields = ['nombre']
    list_filter = ['tipo']

# @admin.register(Auto)
# class AutoAdmin(admin.ModelAdmin):
#     pass


# @admin.register(Ficha, Hero, Caracteristica, Prestacion)
# class FichaAdmin(admin.ModelAdmin):
#     pass
