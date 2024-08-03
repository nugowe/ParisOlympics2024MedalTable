from django.shortcuts import render
from django import forms

class MedalTableForm(forms.Form):
    Country = forms.CharField()
    


    