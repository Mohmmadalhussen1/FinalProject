from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return f"Profile of {self.user.username}"

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    scope = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
# models.py
class SubControl(models.Model):
    name = models.CharField(max_length=255)
    # Other fields as required

class AuditFile(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    sub_control = models.CharField(max_length=255)
    file = models.FileField(upload_to='audit_files/')
    status = models.CharField(
        max_length=50,
        choices=[
            ('implemented', 'Implemented'),
            ('not_implemented', 'Not Implemented'),
            ('semi_implemented', 'Semi Implemented')
        ],
        null=True,
        blank=True
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - {self.sub_control}"