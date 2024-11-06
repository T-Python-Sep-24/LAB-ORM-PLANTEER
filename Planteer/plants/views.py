from django.shortcuts import render, redirect
from django.http import HttpRequest

#New plant view 
def newPlantView(request:HttpRequest):
    
    return render(request, 'plants/newPlant.html')