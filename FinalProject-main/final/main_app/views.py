# Create your views here.
# views.py
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from .models import Domain,Control
from django.shortcuts import render


from io import BytesIO
from django.template.loader import render_to_string
from xhtml2pdf import pisa  # You can use a PDF library like xhtml2pdf for easier HTML-to-PDF conversion.

@csrf_protect
def home_page(request):
    return render(request, 'main_app/home_page.html')  

def tree_view(request):
    """Render the interactive tree."""
    domains = Domain.objects.prefetch_related('subdomains__controls').all()
    return render(request, 'main_app/tree.html', {'domains': domains})

def control_detail(request, pk):
    """Display control details."""
    control = get_object_or_404(Control, pk=pk)
    if request.method == "POST":
        # Handle control updates
        control.name = request.POST.get('name', control.name)
        control.description = request.POST.get('description', control.description)
        control.save()
    return render(request, 'main_app/control_detail.html', {'control': control})
