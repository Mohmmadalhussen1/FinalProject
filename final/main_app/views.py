from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
# Create your views here.
# views.py

def home_page(request):
    return render(request, 'main_app/home_page.html')

def sessions_page(request):
    return render(request, 'main_app/sessions_page.html')

def report_generation_page(request):
    return render(request, 'main_app/report_generation_page.html')

def policy_review(request):
    return render(request, 'main_app/policy_review.html')

def sign_up_page(request):
    return render(request, 'main_app/sign_up_page.html')

def tree_page(request):
    return render(request, 'main_app/tree.html')

def login_page(request: HttpRequest):
    if request.user.is_authenticated:
        print(request.user.username)
        return redirect("main_app:home_page")
    # if user login already redirect to home page

    msg = None
    if request.method == "POST":
        user: User = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user:
            login(request, user)
            return redirect("main_app:home_page")
        else:
            msg = "Incorrect Credentials"

    return render(request, "main_app/login_page.html", {"msg": msg})


def signout_page(request):
    logout(request)
    return redirect('main_app:login_page')  # Redirect to login page after sign out