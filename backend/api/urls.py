from django.urls import path,include
from .views import *

urlpatterns = [
    path('collect/',CollectDataViews.as_view(),name="collect"),
    path('similar/',CalculateSimilartyView.as_view(),name="similarity"),
]