from django.contrib import admin

from .models import MedalTable

@admin.register(MedalTable)
class MedalTableAdmin(admin.ModelAdmin):
    list_display = ('Rank','Country', 'Flag', 'Gold', 'Silver', 'Bronze', 'Total')
    search_fields = ('Rank','Country', 'Flag', 'Gold', 'Silver', 'Bronze', 'Total')
# Register your models here.
