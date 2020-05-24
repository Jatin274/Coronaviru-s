from django.shortcuts import render  
from .models import *




def Index(request):
    today= News.objects.all()
    d={
        "news":today
    }
    return render(request,"Jatin/index.html",d)

def ArogyaSetuApp(request):
    return render(request,"Jatin/arogyasetu.html")



