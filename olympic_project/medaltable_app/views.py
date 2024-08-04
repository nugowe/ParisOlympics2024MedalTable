from django.shortcuts import render
from medaltable_app.models import MedalTable
from medaltable_app.forms import MedalTableForm
from datetime import datetime
from django.http import HttpResponse
from medaltable_app.filters import MedalTableFilter


def BackEndMedalTable(request):
    MedalTable_filter =  MedalTableFilter(request.GET, queryset=MedalTable.objects.all())
    context = {
        'form': MedalTable_filter.form,
        'medaltables': MedalTable_filter.qs 
    }
    return render (request, 'medaltable.html', context)


def GamesDuration(request):
    target_date = datetime(2024, 8, 11)
    current_datetime = datetime.now()
    time_left = target_date - current_datetime
    
    days = time_left.days
    hours = time_left.seconds // 3600
    minutes = time_left.seconds // 60 % 60
    seconds = time_left.seconds % 60

    return HttpResponse(f"<h3><i><strong>THE GAMES END IN </strong> {days} days, {hours} hours, {minutes} minutes, {seconds} seconds....</i></h3>")



def GamesPercentage(request):
    EPLStartDate = datetime(2024, 7, 24, 21, 0)  
    EPLEndDate = datetime(2024, 8, 11, 0, 0)   
    EPLDuration = (EPLEndDate - EPLStartDate).days
    CurrentDate = datetime.now()
    EPLDurationTillDate = (EPLEndDate - CurrentDate).days
    EPLElapsedDays = EPLDuration - EPLDurationTillDate
    PercentagePlayingdaysleft = (EPLElapsedDays / EPLDuration) * 100
    PercentagePlayingdaysleft = round(PercentagePlayingdaysleft, 0)
    return HttpResponse(f"<h3><i>ABOUT <strong>{PercentagePlayingdaysleft}%</strong> OF EVENT DAYS LEFT!....</i></h3>")
