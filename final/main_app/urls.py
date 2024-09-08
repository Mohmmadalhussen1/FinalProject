from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
    path('sign_up_page/', views.sign_up_page, name='sign_up_page'),
    path('sessions_page/', views.sessions_page, name='sessions_page'),
    path('report_generation_page/', views.report_generation_page, name='report_generation_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('policy_review/', views.policy_review, name='policy_review'),
    path('tree/', views.tree_page, name='tree'),
    path('', views.home_page, name='home_page'),
    path('signout/', views.signout_page, name='signout_page'),

]
