from django.urls import path
from . import views

app_name = "main_app"

urlpatterns = [
        path("", views.index, name="index"),
        path("controls", views.controls, name="controls"),
    path("attack", views.attack_navigator, name="attack_navigator"),
    # Add any other URL patterns as needed


]