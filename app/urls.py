from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('keitai',views.keitai,name="keitai"),
    path('result',views.result,name="result"),
]
