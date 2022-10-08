from turtle import update
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns =[
    path('',views.readtask),
    path('create/',views.addtask),
    path('update/<title>',views.updatetask),
    path('delete/<title>',views.deletetask)
]
    
