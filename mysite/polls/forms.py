from django import forms
from django.db import models

class formDice(forms.Form):
    superficiemin = forms.IntegerField(label='superficiemin',required=False)
    localisation = forms.IntegerField(label = 'localisation',required=False) 




