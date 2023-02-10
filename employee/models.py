from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name=models.CharField(max_length=100, null=True, blank=True)
    last_name=models.CharField(max_length=100, null=True, blank=True)
    profile_picture=models.ImageField(null=True, default='profiles/man.png')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str((self.first_name))
    

class Employee(models.Model):
    ROLES = (
    ('manager', 'Manager'),
    ('manager', 'Vice Manager'),
    ('other_employee', 'Other Employee'),
)
    employee = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=100, null=True, blank=True, choices=ROLES)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str((self.employee.first_name, self.employee.last_name))
    
    
class Message(models.Model):
    sender = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ManyToManyField(Employee,  blank=True, related_name="messages")
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.subject)
    
    
def createProfile(sender, instance, created, **kwargs):
    if created:
        user=instance
        user_id = user.id
        
        profile = Profile.objects.create( 
            user=user,
            first_name = user.first_name,
            last_name= user.last_name,
            email=user.email,

        )

        
        
def editProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    
    if created == False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.email = profile.email
        user.save()
        

        
        
def deleteUser(sender, instance, **kwargs):
    try:
        user=instance.user
        user.delete()
    except:
        pass
    
        
post_save.connect(createProfile, sender=User)
post_save.connect(editProfile, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)