from django.db import models
from django.db.models.fields import json
from django.db.models import JSONField
# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    latitude=models.DecimalField(max_digits=22,decimal_places=16,blank=True,null=True,default=28.644800)
    longitude= models.DecimalField(max_digits=22,decimal_places=16,blank=True,null=True,default=28.644800)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Citys"


class HourlyData(models.Model):
    city = models.ForeignKey('City',null=True,blank=True,related_name='api_city',on_delete=models.CASCADE)
    dt=models.FloatField(null=True, blank=True, default=0)
    temp=models.FloatField(null=True, blank=True, default=0)
    feels_like=models.FloatField(null=True, blank=True, default=0)
    pressure=models.FloatField(null=True, blank=True, default=0)
    humidity=models.FloatField(null=True, blank=True, default=0)
    dew_point=models.FloatField(null=True, blank=True, default=0)
    uvi=models.FloatField(null=True, blank=True, default=0)
    clouds=models.FloatField(null=True, blank=True, default=0)
    visibility=models.FloatField(null=True, blank=True, default=0)
    wind_speed=models.FloatField(null=True, blank=True, default=0)
    wind_deg=models.FloatField(null=True, blank=True, default=0)
    wind_gust=models.FloatField(null=True, blank=True, default=0)
    weather=JSONField(null=True, blank=True, default=dict)
    
    def __str__(self):
        return str(self.city.name)+str(self.dt)

    class Meta:
        verbose_name = "Hourly"
        verbose_name_plural = "Hourly"