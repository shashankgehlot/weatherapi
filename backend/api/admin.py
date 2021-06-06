from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name","latitude","longitude")

@admin.register(HourlyData)
class HourlyDataAdmin(admin.ModelAdmin):
    list_display = ("id","dt")