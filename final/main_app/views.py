from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
# views.py

def auditor_workflow(request):
    return render(request, 'main_app/auditor_workflow.html')

def program_interaction(request):
    return render(request, 'main_app/program_interaction.html')



def update_controls(request):
    return render(request, 'main_app/update_controls.html')

def control_tree(request):
    return render(request, 'main_app/control_tree.html')