from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('sign_up_page/', views.sign_up_page, name='sign_up_page'),
    path('sessions_page/', views.audit_sessions, name='sessions_page'),
    path('report_generation_page/', views.report_generation_page, name='report_generation_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('policy_review/', views.policy_review, name='policy_review'),
    path('tree/', views.tree_page, name='tree'),
    path('', views.home_page, name='home_page'),
    path("scopedetails/", views.scopeanddetailspage, name="scope-and-detailspage"),
    path('signout/', views.signout_page, name='signout_page'),
    path("profile_page/", views.profile_page, name="profile_page"),
    path('add_company/', views.add_company, name='add_company'),
    
    # Upload Audit File
    path('upload/', views.upload_audit_file, name='upload_audit_file'),
    
    # Checklist Page after file upload
    path('checklist/<int:file_id>/', views.checklist_page, name='checklist_page'),
    
    # Save Checklist Status
    path('save-checklist/', views.save_checklist, name='save_checklist'),
]
