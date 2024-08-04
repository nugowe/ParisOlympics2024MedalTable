import django_filters
from medaltable_app.models import MedalTable

class MedalTableFilter(django_filters.FilterSet):
    class Meta:
        model = MedalTable
        fields = {
            'Country'
            
        }