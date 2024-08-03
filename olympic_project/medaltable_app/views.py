from django.shortcuts import render
from medaltable_app.models import MedalTable
from medaltable_app.forms import MedalTableForm

def BackEndMedalTable(request):
    MedalTableQuery = request.GET.get('Medal_Table_Query')
    AllMedals = MedalTable.objects.all().distinct()
    if MedalTableQuery:
        AllMedals = AllMedals.filter(Country__icontains=MedalTableQuery)
    context = {
        'form': MedalTableForm(),
        'medaltables': AllMedals 
    }
    return render (request, 'medaltable.html', context)



def MedalTableRefresh(request):
    MedalTableQuery = request.GET.get('Medal_Table_Query')
    AllMedals = MedalTable.objects.all().distinct()
    if MedalTableQuery:
        AllMedals = AllMedals.filter(Country__icontains=MedalTableQuery)
    context = {
        'form': MedalTableForm(),
        'medaltables': AllMedals 
    }
    return render (request, 'medaltable.html', context)