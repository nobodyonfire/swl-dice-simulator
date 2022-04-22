from django.urls import path
from . import views


app_name = 'swl'
urlpatterns = [
    path('', views.globalRequest, name='index'),
    path('stats', views.statsRequest, name='stats'),
    path('infos', views.infosRequest, name='infos'),

]