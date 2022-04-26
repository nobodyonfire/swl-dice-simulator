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

        form = formDice(request.POST)
            



        numberAttRedDice = request.POST.get('ratt', 0)
        numberAttBlackDice = request.POST.get('natt', 0)
        numberAttWhiteDice = request.POST.get('watt', 0)

        AdreConvertCrit = request.POST.get('adrecrit', 0)
        AdreConvert = request.POST.get('adretouche', 0)
        HauteVelocite = request.POST.get('hautevelocite', 0)

        DefDiceUsed = request.POST.get('defdices', 0)
        
        surgeNumber = request.POST.get('surge', 0)
        critiqueNumber = request.POST.get('critical', 0)
        impactNumber = request.POST.get('impact', 0)
        perforantNumber = request.POST.get('perforant', 0)

        adredef= request.POST.get('adredef',0)
        fullArmor = request.POST.get('fullarmure', 0)
        armorNumber = request.POST.get('armure', 0)
        dodgeNumber = request.POST.get('dodge', 0)
        couvertNumber = request.POST.get('couvert', 0)
        dangersensNumber = request.POST.get('dangersens', 0)
        coupdechanceNumber = request.POST.get('coupdechance', 0)
        surgeDefNumber = request.POST.get('surgedef', 0)
        aimNumber = request.POST.get('aim', 0)
        preciseNumber = request.POST.get('precise', 0)
        manoimpro = request.POST.get('manoimpro', 0)
        
        

        numberAttRedDice=trad(numberAttRedDice)
        numberAttBlackDice=trad(numberAttBlackDice)
        numberAttWhiteDice=trad(numberAttWhiteDice)
        AdreConvertCrit=tradCheckBox(AdreConvertCrit)
        AdreConvert=tradCheckBox(AdreConvert)
        HauteVelocite=tradCheckBox(HauteVelocite)
        manoimpro=tradCheckBox(manoimpro)
    
        adredef=tradCheckBox(adredef)
        fullArmor=tradCheckBox(fullArmor)

        critiqueNumber=trad(critiqueNumber)
        impactNumber=trad(impactNumber)
        perforantNumber=trad(perforantNumber)

        armorNumber=trad(armorNumber)
        dodgeNumber=trad(dodgeNumber)
        couvertNumber=trad(couvertNumber)
        dangersensNumber=trad(dangersensNumber)
        coupdechanceNumber=trad(coupdechanceNumber)
        surgeNumber=trad(surgeNumber)
        surgeDefNumber=trad(surgeDefNumber)
        aimNumber=trad(aimNumber)
        preciseNumber=trad(preciseNumber)


        resultedEsperance,crits,hits,miss,wounds,numbersaves = throwDice(numberAttWhiteDice,numberAttBlackDice,numberAttRedDice,DefDiceUsed,fullArmor,adredef,manoimpro,\
                 AdreCrit=AdreConvertCrit,Adre=AdreConvert,critiqueNumber = critiqueNumber,impactNumber=impactNumber,armorNumber=armorNumber,dodgeNumber=dodgeNumber,couvertNumber=couvertNumber,perforantNumber=perforantNumber,dangersensNumber=dangersensNumber,coupdechanceNumber=coupdechanceNumber,surgeNumber=surgeNumber,surgeDefNumber=surgeDefNumber,HauteVelocite=HauteVelocite,aimNumber=aimNumber,preciseNumber=preciseNumber)  


        


        print("Resulted Esperance : ", resultedEsperance)
        dict= {
            'output':True,
            'outputatt':True,
            'resultedEsperance':round(resultedEsperance,2),
            'crits':round(crits,2),
            'hits':round(hits,2),
            'miss':round(miss,2),
            'wounds':round(wounds,2),
            'numbersaves':round(numbersaves,2),

            'armorNumber':armorNumber ,
            'dodgeNumber':dodgeNumber,
            'fullArmor':fullArmor,
            'couvertNumber':couvertNumber


        
            }
        
        return render(request, 'polls/index.html',dict)  



