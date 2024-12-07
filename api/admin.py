from django.contrib import admin
from .models import *


# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "continent",
        "created_at",
        "updated_at",
    )


admin.site.register(Country, CountryAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "created_at",
        "updated_at",
    )


admin.site.register(City, CityAdmin)
