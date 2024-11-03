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
    description = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    scope = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)

class AuditFile(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sub_control = models.CharField(max_length=255)
    file = models.FileField(upload_to='audit_files/')
    status = models.CharField(max_length=50, choices=[
        ('implemented', 'Implemented'),
        ('not_implemented', 'Not Implemented'),
        ('semi_implemented', 'Semi Implemented')
    ])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    
    def __str__(self) -> str:
        return f"{self.user.username}"
