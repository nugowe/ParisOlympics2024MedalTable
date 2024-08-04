from django.urls import path
from . import views

urlpatterns = [
    path('', views.BackEndMedalTable, name='BackEndMedalTable'),
    path('gamesduration/', views.GamesDuration, name='GamesDuration'),
    path('gamespercentage/', views.GamesPercentage, name='GamesPercentage')
]