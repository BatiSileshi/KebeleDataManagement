from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Employee(models.Model):
    ROLES = (
        ('Hoji geggeessaa', 'Hoji geggeessaa'),
        ('To\'ataa', 'To\'ataa'),
        ('Barreessaa', 'Barreessaa'),
    )
    
    employee = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name=models.CharField(max_length=100, null=True, blank=True)
    last_name=models.CharField(max_length=100, null=True, blank=True)
    profile_picture=models.ImageField(null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    role = models.CharField(max_length=100, null=True, blank=True, choices=ROLES)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str((self.first_name, self.role))
    

  
    
class Message(models.Model):
    sender = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.subject)