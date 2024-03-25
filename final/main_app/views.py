from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def index(request:HttpRequest):
    
# Home HTML

    return render(request, "main_app/index.html")

def controls(request:HttpRequest):
    
# Home HTML

    return render(request, "main_app/controls.html")

from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse

def attack_navigator(request: HttpRequest):
    Domains = [
        'Domain: Cybersecurity Governance',
        'Domain: Cybersecurity Defense',
        'Domain: Cybersecurity Resilience',
        'Domain: Third-Party and Cloud Computing Cybersecurity',
        'Domain: ICS Cybersecurity (Industrial Control Systems)',
    ]
    index_url = reverse("main_app:index")

    # Generating URLs for Govcons and Defcons pointing to the index page
    govcons = [
        ('1-1 Cybersecurity Strategy', 'controls'),
        ('1-2 Cybersecurity Management', ''),
        ('1-3 Cybersecurity Policies and Procedures', ''),
        ('1-4 Cybersecurity Roles and Responsibilities', ''),
    ]
    
    defcons = [
        ('1-1 Cybersecurity Strategy', ''),
        ('1-2 Cybersecurity Management', ''),
        ('1-3 Cybersecurity Policies and Procedures', ''),
        ('1-4 Cybersecurity Roles and Responsibilities', ''),
    ]

    return render(request, 'main_app/attack_navigator.html', {'Domains': Domains, 'Govcons': govcons, 'Defcons': defcons})