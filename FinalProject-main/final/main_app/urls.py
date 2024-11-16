from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # Import this line
app_name = "main_app"

urlpatterns = [
    path('sign_up_page/', views.sign_up_page, name='sign_up_page'),
        
    path('report_generation_page/', views.report_generation_page, name='report_generation_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('policy_review/', views.policy_review, name='policy_review'),
    path('tree/', views.tree_page, name='tree'),
    path('', views.home_page, name='home_page'),
    path("scopedetails/", views.scopeanddetailspage, name="scope-and-detailspage"),
    path('signout/', views.signout_page, name='signout_page'),
    path("profile_page/", views.profile_page, name="profile_page"),
    path('add_company/', views.add_company, name='add_company'),
    path('sessions/', views.audit_sessions, name='sessions_page'),
    path('checklist/<int:company_id>/<str:sub_control>/', views.checklist_page, name='checklist_page'),
    path('remove_audit_file/<int:file_id>/', views.remove_audit_file, name='remove_audit_file'),
    path('upload_audit_files/', views.upload_audit_files, name='upload_audit_files'),
    # Save Checklist Status
    path('save-checklist/', views.save_checklist, name='save_checklist'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
