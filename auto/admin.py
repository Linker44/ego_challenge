from django.contrib import admin
from auto.models import Auto, Ficha, Caracteristica

# Register your models here.


class AutoAdmin(admin.ModelAdmin):
    pass


class FichaAdmin(admin.ModelAdmin):
    pass


class CaracteristicaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Auto, AutoAdmin)
admin.site.register(Ficha, FichaAdmin)
admin.site.register(Caracteristica, CaracteristicaAdmin)
