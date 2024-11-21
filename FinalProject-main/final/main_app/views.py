# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Company, AuditFile  
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Company  # Ensure this is here
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Company, AuditFile
from django.db import IntegrityError
from django.http import JsonResponse
from .models import SubControl
from django.shortcuts import render
from django.http import HttpResponse
from .models import Company, AuditFile
from io import BytesIO
from django.template.loader import render_to_string
from xhtml2pdf import pisa  # You can use a PDF library like xhtml2pdf for easier HTML-to-PDF conversion.

@csrf_protect
def home_page(request):
    return render(request, 'main_app/home_page.html')


from django.http import JsonResponse
from .models import Company, AuditFile

from django.http import JsonResponse
from .models import Company, AuditFile

# In views.py
from django.http import JsonResponse

# In views.py
from django.http import JsonResponse
from .models import SubControl, AuditFile

def fetch_subcontrols(request):
    company_id = request.GET.get('company_id')
    print(f"Fetching sub-controls for company_id: {company_id}")  # Debug line
    subcontrols = SubControl.objects.filter(company_id=company_id)
    subcontrol_data = []
    for subcontrol in subcontrols:
        files = AuditFile.objects.filter(sub_control=subcontrol)
        subcontrol_data.append({
            'name': subcontrol.name,
            'files': [{'file': file.file.url, 'status': file.status, 'id': file.id} for file in files]
        })
    print(f"Sub-controls data: {subcontrol_data}")  # Debug line
    return JsonResponse({'subcontrols': subcontrol_data})


def generate_report_page(request):
    # Fetch the company (assuming a single company or the one currently logged in)
    company = Company.objects.first()  # Replace with logic to fetch the correct company
    sub_controls = AuditFile.objects.filter(company=company)  # Fetch sub-controls for the company

    # Pass the data to the template
    context = {
        "company": company,
        "sub_controls": sub_controls,
    }
    return render(request, "generate_report.html", context)


def generate_summary_pdf(company, comments):
    html_content = render_to_string("summary_template.html", {
        'company': company,
        'comments': comments
    })
    
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="summary_report.pdf"'
    
    pisa_status = pisa.CreatePDF(html_content, dest=response)
    
    return response

def generate_detailed_report(request):
    if request.method == "POST":
        # Fetch user inputs (replace these keys with your actual form/input names)
        company_name = request.POST.get("company_name")
        description = request.POST.get("description")
        scope = request.POST.get("scope")
        subcontrols = request.POST.getlist("subcontrols")  # List of subcontrol names
        statuses = request.POST.getlist("statuses")  # Corresponding statuses for subcontrols

        # Prepare context for the template
        context = {
            "company_name": company_name,
            "description": description,
            "scope": scope,
            "subcontrols": zip(subcontrols, statuses),
        }

        # Render the HTML content
        html_content = render_to_string("detailed_report_template.html", context)

        # Generate PDF
        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'inline; filename="detailed_report.pdf"'
        pisa_status = pisa.CreatePDF(BytesIO(html_content.encode("utf-8")), dest=response)

        if pisa_status.err:
            return HttpResponse("Error generating PDF", status=500)
        return response

    # Render the form page if GET request
    return render(request, "generate_report_form.html")
    
    response = HttpResponse(content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename="detailed_report.pdf"'
    
    pisa_status = pisa.CreatePDF(html_content, dest=response)
    
    return response

# views.py
from .models import Company
from django.shortcuts import render, redirect

def add_company(request):
     # Get the company information and save the company 
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

    # Fetch all audit files grouped by sub-control
    sub_controls_with_files = []
    for control in sub_controls:
        files = AuditFile.objects.filter(company=company, sub_control=control)
        sub_controls_with_files.append({
            'name': control,
            'files': files  # Include all files for the sub-control
        })

    return render(request, 'main_app/sessions_page.html', {
        'company_name': company_name,
        'sub_controls_with_files': sub_controls_with_files,
        'company': company
    })

def remove_audit_file(request, file_id):
    file = AuditFile.objects.get(id=file_id)
    file.delete()
    return redirect('main_app:sessions_page')
    
# List of sub-controls
sub_controls_list = [
    "1-1 Cybersecurity Strategy",
    "1-2 Cybersecurity Management",
    "2-1 Asset Management",
    "2-4 Email Protection",
    "2-5 Network Security Management"
]

def upload_audit_files(request):
    if request.method == 'POST' and request.FILES.get('files'):
        company_id = request.POST.get('company_id')
        sub_control = request.POST.get('sub_control')

        # Ensure that the sub_control exists in the predefined list
        if sub_control not in sub_controls_list:
            return HttpResponse("Invalid sub-control", status=400)

        # Retrieve the company instance based on company_id
        company = Company.objects.get(id=company_id)

        # Process the uploaded files
        uploaded_files = request.FILES.getlist('files')
        for uploaded_file in uploaded_files:
            # Create an AuditFile object and save each file
            AuditFile.objects.create(
                company=company,
                sub_control=sub_control,
                file=uploaded_file,
                status='pending'  # Assuming 'pending' is the default status
            )

        # Redirect to checklist page with company_id and sub_control to show uploaded files
        return redirect('main_app:checklist_page', company_id=company_id, sub_control=sub_control)

    return HttpResponse("Invalid request", status=400)
    
def checklist_page(request, company_id, sub_control):
    # Retrieve the company instance
    company = get_object_or_404(Company, id=company_id)

    # Get the files associated with the given company and sub-control
    audit_files = AuditFile.objects.filter(company=company, sub_control=sub_control)

    return render(request, 'main_app/checklist_page.html', {
        'company': company,
        'sub_control': sub_control,
        'audit_files': audit_files
    })

def save_checklist(request):
    if request.method == 'POST':
        file_id = request.POST.get('file_id')
        status = request.POST.get('status')

        # Find the AuditFile and update its status
        audit_file = AuditFile.objects.get(id=file_id)
        audit_file.status = status
        audit_file.save()

        # Redirect back to the checklist page after saving the status
        return redirect('main_app:checklist_page', company_id=audit_file.company.id, sub_control=audit_file.sub_control)

    return redirect('main_app:home')  # Fallback, in case the request isn't POST
    
@csrf_protect
def report_generation_page(request):
    company = Company.objects.first()  # Fetch the first company
    if not company:
        return HttpResponse("No company found.", status=404)

    subcontrols = AuditFile.objects.filter(company=company)
    context = {
        "company": company,
        "subcontrols": subcontrols,
    }
    return render(request, "main_app/report_generation_page.html", context)

@csrf_protect
def policy_review(request):
    return render(request, 'main_app/policy_review.html')
from django.shortcuts import render

def tree_view(request):
    # Example data structure for the tree
    tree_data = {
        "name": "Root Node",
        "children": [
            {
                "name": "Branch 1",
                "children": [
                    {"name": "Sub-Branch 1.1", "children": []},
                    {"name": "Sub-Branch 1.2", "children": []},
                ],
            },
            {
                "name": "Branch 2",
                "children": [
                    {"name": "Sub-Branch 2.1", "children": []},
                ],
            },
            {"name": "Branch 3", "children": []},
        ],
    }
    return render(request, "main_app/tree.html", {"tree_data": tree_data})

@csrf_protect
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

@csrf_protect
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

@csrf_protect
def signout_page(request):
    logout(request)
    return redirect('main_app:login_page')  # Redirect to login page after sign out

@csrf_protect
def profile_page(request:HttpRequest):

        #Show each  data inside the model in thier ID


    return render(request, 'main_app/user_details.html') 