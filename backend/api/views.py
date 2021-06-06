from django.http import response
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from .models import *
from django.db.models import Avg, Max, Min
import requests

class CollectDataViews(APIView):
    def get(self, request):
        for i in City.objects.all().order_by("-id"):
            response=requests.get(url=f'https://api.openweathermap.org/data/2.5/onecall?lat={i.latitude}&lon={i.longitude}&exclude=monthly,daily,current,minutely&appid=fad2242deeb0e1143cb2a4e3b0b36e7e')
            data=response.json()
            for k in data['hourly']:
                obj,created=HourlyData.objects.get_or_create(dt=k['dt'],city=i)
                if obj:
                    obj.temp = k['temp']
                    obj.feels_like = k['feels_like']
                    obj.pressure = k['pressure']
                    obj.humidity = k['humidity']
                    obj.dew_point = k['dew_point']
                    obj.uvi = k['uvi']
                    obj.clouds = k['clouds']
                    obj.visibility = k['visibility']
                    obj.wind_speed = k['wind_speed']
                    obj.wind_deg = k['wind_deg']
                    obj.wind_gust = k['wind_gust']
                    obj.weather = k['weather']
                    obj.save()
        return Response("Data Saved Successfully of last 48 Hours",status=status.HTTP_200_OK)

def checkabs(a,b):
    if abs(a-b)<=0.7 and abs(a-b)!=0:
        return True
    else:
        False

class CalculateSimilartyView(APIView):
    def get(self, request):
        list=[]
        for i in City.objects.all():
            data=HourlyData.objects.filter(city=i).order_by('-id')[:48].aggregate(Avg('temp'),Avg('pressure'),Avg('humidity'),Avg('dew_point'))
            data['city']=i.name
            list.append(data)
        return Response(list,status=status.HTTP_200_OK)



