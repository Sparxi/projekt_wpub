from django.urls import path, include

from . import views

urlpatterns = [

    path("", views.index, name ='index'),
    path("vzostupne/", views.zorad_vzostupne, name='vzostupne'),
    path('zostupne/', views.zorad_zostupne, name='zostupne'),

]

