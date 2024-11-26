from django.db import models
from django.contrib.auth.models import User

# models.py
from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=255)

class Subdomain(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='subdomains')
    name = models.CharField(max_length=255)

class Control(models.Model):
    subdomain = models.ForeignKey(Subdomain, on_delete=models.CASCADE, related_name='controls')
    name = models.CharField(max_length=255)
    description = models.TextField()

    # New fields
    section = models.CharField(max_length=255, blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    implementation_steps = models.TextField(blank=True, null=True)
    examples = models.TextField(blank=True, null=True)
    tools = models.TextField(blank=True, null=True)
    deliverables = models.TextField(blank=True, null=True)

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