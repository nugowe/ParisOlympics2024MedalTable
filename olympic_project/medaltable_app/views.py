from django.shortcuts import render
from medaltable_app.models import MedalTable
from medaltable_app.forms import MedalTableForm

def BackEndMedalTable(request):
    context = {
        'form': MedalTableForm(),
        'medaltables': MedalTable.objects.all()
    }
    return render (request, 'medaltable.html', context)


