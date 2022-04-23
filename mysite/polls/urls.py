from django.urls import path
from . import views


app_name = 'swl'
urlpatterns = [
    path('', views.globalRequest, name='index'),
    path('outputatt', views.outputattRequest, name='outputatt'),
    path('outputdef', views.outputdefRequest, name='outputdef'),

]