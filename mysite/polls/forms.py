from django import forms
from django.db import models

class SurveyForm(forms.Form):
    occupantsmin = forms.IntegerField(label='occupantsmin',required=False)
    occupantsmax = forms.IntegerField(label='occupantsmax',required=False)
    superficiemin = forms.IntegerField(label='superficiemin',required=False)
    superficiemax = forms.IntegerField(label='superficiemax',required=False)
    localisation = forms.IntegerField(label = 'localisation',required=False) 
    type = forms.CharField(label='type',required=False)
    heating = forms.CharField(label='heating',required=False)


