from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Company, AuditFile  # Make sure to include all necessary models
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import JsonResponse

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
from .models import Company  # Ensure this is here

# Create your views here.
# views.py


def home_page(request):
    return render(request, 'main_app/home_page.html')


# views.py
from .models import Company
from django.shortcuts import render, redirect

def add_company(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description', '')
        contact_number = request.POST.get('contact_number')
        scope = request.POST.get('scope', '')
        details = request.POST.get('details', '')

        new_company = Company(
            name=name,
            description=description,
            contact_number=contact_number,
            scope=scope,
            details=details,
        )
        new_company.save()
        return redirect("main_app:sessions_page")

    return render(request, 'main_app/add_company.html')

    
    
def scopeanddetailspage(request):
    if request.method == "POST":
        # Get selected company and updated values from the form
        company_id = request.POST.get('company-select')
        scope = request.POST.get('scope-comments')
        description = request.POST.get('description')
        sub_controls = request.POST.getlist('sub-controls')

        # Update the company fields
        company = Company.objects.get(id=company_id)
        company.scope = scope
        company.description = description
        company.save()

        # Store selected company ID and sub-controls in the session
        request.session['selected_company_id'] = company_id
        request.session['selected_sub_controls'] = sub_controls

        # Redirect to the sessions page
        return redirect('main_app:sessions_page')

    # If GET request, retrieve companies
    companies = Company.objects.all()
    sub_controls_list = ["1-1 Cybersecurity Strategy", "1-2 Cybersecurity Management", "2-1 Asset Management","2-4 Email Protection","2-5 Network Security Management"]  # Example list of sub-controls
    return render(request, 'main_app/scope-and-detailspage.html', {
        'companies': companies,
        'sub_controls_list': sub_controls_list
    })

def audit_sessions(request):
    company_id = request.session.get('selected_company_id')
    sub_controls = request.session.get('selected_sub_controls', [])

    company = Company.objects.get(id=company_id) if company_id else None
    company_name = company.name if company else "No company selected"

    return render(request, 'main_app/sessions_page.html', {
        'company_name': company_name,
        'sub_controls': sub_controls,
        'company': company  # Pass company to context
    })


# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Company, AuditFile
from django.core.files.storage import default_storage

def upload_audit_file(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        sub_control = request.POST.get('sub_control')
        file = request.FILES.get('file')

        if not company_id:
            return HttpResponse("Company ID is missing.", status=400)
        
        if not sub_control:
            return HttpResponse("Sub-control is missing.", status=400)
        
        if not file:
            return HttpResponse("File is missing.", status=400)

        # Use get_object_or_404 to fetch the Company object
        company = get_object_or_404(Company, id=company_id)

        # Save the file to AuditFile model
        audit_file = AuditFile.objects.create(
            company=company,
            sub_control=sub_control,
            file=file,
            status='not_implemented'  # Default status for new uploads
        )

        return redirect(reverse('main_app:checklist_page', args=[audit_file.id]))
    else:
        return HttpResponse("Invalid request method.", status=405)


def checklist_page(request, audit_file_id):
    # Retrieve the uploaded audit file and related data for the checklist page
    audit_file = get_object_or_404(AuditFile, id=audit_file_id)
    return render(request, 'main_app/checklist_page.html', {
        'uploaded_file_url': audit_file.file.url,
        'company': audit_file.company,
        'sub_control': audit_file.sub_control
    })


def save_checklist(request):
    if request.method == 'POST':
        company_id = request.POST.get('company_id')
        sub_control = request.POST.get('sub_control')
        status = request.POST.get('status')

        # Validate input data
        if not company_id or not sub_control or not status:
            return HttpResponse("Required data is missing.", status=400)

        # Update the status for the relevant sub-control in AuditFile
        audit_file = AuditFile.objects.filter(
            company_id=company_id,
            sub_control=sub_control
        ).first()

        if audit_file:
            audit_file.status = status
            audit_file.save()

        return redirect('main_app:sessions')  # Redirect to sessions page
    return HttpResponse("Invalid request method.", status=405)

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