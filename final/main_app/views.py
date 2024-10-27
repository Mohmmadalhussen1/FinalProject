from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
# views.py


def home_page(request):
    return render(request, 'main_app/home_page.html')

def scopeanddetailspage(request):
    return render(request, 'main_app/scope-and-detailspage.html')

def sessions_page(request):
    return render(request, 'main_app/sessions_page.html')

def report_generation_page(request):
    return render(request, 'main_app/report_generation_page.html')

def policy_review(request):
    return render(request, 'main_app/policy_review.html')

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


def sign_up_page(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
        email = request.POST['email']
        phone = request.POST['phone']  # You may need to handle this with a custom user model

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            msg = 'Username already taken'
        elif User.objects.filter(email=email).exists():
            msg = 'Email already taken'
        else:
            # Create new user
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

    else:
        msg = None

    return render(request, 'main_app/sign_up_page.html')


def signout_page(request):
    logout(request)
    return redirect('main_app:login_page')  # Redirect to login page after sign out

def profile_page(request:HttpRequest):

        #Show each  data inside the model in thier ID


    return render(request, 'main_app/user_details.html') 