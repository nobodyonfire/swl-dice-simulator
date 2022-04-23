# Create your views here.
from re import A
from urllib import response
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader 
from .models import Choice, Question,UID
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.forms import ModelForm
from .forms import formDice

from .pythonalgorithms.functions import *


from django.shortcuts import render



def globalRequest(request):

    if request.method == 'GET':
        
        dictGlobal = { 
        }


        return render(request, 'polls/index.html',dictGlobal)  

    if request.method == 'POST':

  
        dictGlobal= {
        }
        return render(request, 'polls/index.html',dictGlobal)  

def trad(x):
    if x:
        x=int(x)
    else:
        x=0
    return x

def tradCheckBox(x):
    if x:
        x=True
    else :
        x=False
    return x

def outputattRequest(request):

    if request.method == 'GET':

        
        dictGlobal = { 
            'output':False
        }

        return render(request, 'polls/index.html',dictGlobal)  

    if request.method == 'POST':


        numberAttRedDice = request.POST.get('ratt', 0)
        numberAttBlackDice = request.POST.get('natt', 0)
        numberAttWhiteDice = request.POST.get('watt', 0)

        AdreConvertCrit = request.POST.get('adrecrit', 0)
        AdreConvert = request.POST.get('adretouche', 0)

        DefDiceUsed = request.POST.get('defdices', 0)

        critiqueNumber = request.POST.get('critical', 0)
        impactNumber = request.POST.get('impact', 0)

        fullArmor = request.POST.get('fullarmure', 0)
        armorNumber = request.POST.get('armure', 0)

        numberAttRedDice=trad(numberAttRedDice)
        numberAttBlackDice=trad(numberAttBlackDice)
        numberAttWhiteDice=trad(numberAttWhiteDice)
        AdreConvertCrit=tradCheckBox(AdreConvertCrit)
        AdreConvert=tradCheckBox(AdreConvert)

        fullArmor=tradCheckBox(fullArmor)

        critiqueNumber=trad(critiqueNumber)
        impactNumber=trad(impactNumber)
        armorNumber=trad(armorNumber)

        
    

        resultedEsperance,crits,hits,miss = throwDice(numberAttWhiteDice,numberAttBlackDice,numberAttRedDice,DefDiceUsed,fullArmor,AdreCrit=AdreConvertCrit,Adre=AdreConvert,critiqueNumber = critiqueNumber,impactNumber=impactNumber,armorNumber=armorNumber)  

        print("Resulted Esperance : ", resultedEsperance)
        dict= {
            'output':True,
            'outputatt':True,
            'resultedEsperance':round(resultedEsperance,2),
            'crits':round(crits,2),
            'hits':round(hits,2),
            'miss':round(miss,2),
        
            }
        
        return render(request, 'polls/index.html',dict)  


  