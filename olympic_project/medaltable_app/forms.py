from django.shortcuts import render
from django import forms

class MedalTableForm(forms.Form):
    Medal_Table_Query = forms.CharField()
    


    