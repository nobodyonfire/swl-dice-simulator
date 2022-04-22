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
from .forms import SurveyForm

from .pythonalgorithms.globalcomputing import *



from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter


def globalRequest(request):

    if request.method == 'GET':
        
        dictGlobal = { 
        }


        return render(request, 'polls/index.html',dictGlobal)  

    if request.method == 'POST':
  
        dictGlobal= {
        }
        return render(request, 'polls/index.html',dictGlobal)  


def statsRequest(request):

    if request.method == 'GET':

        returnDict = main()

        return render(request, 'polls/index.html',returnDict)  

    if request.method == 'POST':
  
        dictGlobal= {
        }
        return render(request, 'polls/index.html',dictGlobal)  


def infosRequest(request):

    if request.method == 'GET':
        dictGlobal= {
        }
        return render(request, 'polls/infos.html',dictGlobal)  

    if request.method == 'POST':
  
        dictGlobal= {
        }
        return render(request, 'polls/infos.html',dictGlobal)  

        
