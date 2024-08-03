import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from medaltableparis2024.models import MedalTable


class Command(BaseCommand):
    help = "Loads car data from CSV file"

    def handle(self, *args, **options):
        datafile = settings.BASE_DIR / 'core' / 'data' / 'medaltable_2024.csv'

        with open(datafile) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                MedalTable.objects.get_or_create(Rank=row[0], Country=row[1], Flag=row[2], Gold=row[3],Silver=row[4],Bronze=row[5],Total=row[6])