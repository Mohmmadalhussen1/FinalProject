from django.urls import path
from . import views
from .views import tree_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views  # Import this line
app_name = "main_app"

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path("tree/", views.tree_view, name="tree"),
    path('control/<int:pk>/', views.control_detail, name='control_detail'),
]
