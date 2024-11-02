from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    # address = models.OneToOneField(Address, on_delete=models.CASCADE)

# models.py
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=20)
    scope = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    
    def __str__(self) -> str:
        return f"{self.user.username}"
