from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('auditor_workflow/', views.auditor_workflow, name='auditor_workflow'),
     path('program_interaction/', views.program_interaction, name='program_interaction'),
    path('update_controls/', views.update_controls, name='update_controls'),
    path('', views.control_tree, name='control_tree'),
]
