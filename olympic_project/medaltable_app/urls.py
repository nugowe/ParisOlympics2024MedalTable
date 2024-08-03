from django.urls import path
from . import views

urlpatterns = [
    path('', views.BackEndMedalTable, name='BackEndMedalTable'),
    path('/MedalTableRefresh', views.MedalTableRefresh, name='MedalTableRefresh')
]