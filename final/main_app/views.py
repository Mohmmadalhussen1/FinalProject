from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def index(request:HttpRequest):
    
# Home HTML

    return render(request, "main_app/index.html")

def controls(request:HttpRequest):
    
# Home HTML

    return render(request, "main_app/controls.html")