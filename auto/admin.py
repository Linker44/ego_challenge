from django.contrib import admin
from auto.models import Auto, Ficha, Caracteristicas

# Register your models here.


class AutoAdmin(admin.ModelAdmin):
    pass


class FichaAdmin(admin.ModelAdmin):
    pass


class CaracteristicasAdmin(admin.ModelAdmin):
    pass


admin.site.register(Auto, AutoAdmin)
admin.site.register(Ficha, FichaAdmin)
admin.site.register(Caracteristicas, CaracteristicasAdmin)
