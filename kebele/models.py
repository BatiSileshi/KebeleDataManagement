from django.db import models

# Create your models here.

class Resident(models.Model):
    SAALA=(
        ('Dhiira', 'Dhiira'),
        ('Dhalaa', 'Dhalaa'),    
    )
    
    first_name=models.CharField(max_length=100, null=True, blank=True)
    middle_name=models.CharField(max_length=100, null=True, blank=True)
    last_name=models.CharField(max_length=100, null=True, blank=True)
    photo=models.ImageField(null=True)
    birth_date = models.DateField(null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=20, null=True, blank=True, choices=SAALA)
    edu_level = models.CharField(max_length=200, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.first_name)
    class Meta:
        ordering = ['first_name']
    
    
class Address(models.Model):
    resident = models.OneToOneField(Resident, on_delete=models.CASCADE, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    hnum = models.CharField(max_length=20, null=True, blank=True)
    kebele = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    zone = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.resident)
    class Meta:
        ordering = ['resident']
    
    
class House(models.Model):
    owner = models.ForeignKey(Resident, on_delete=models.CASCADE, null=True, blank=True)
    hnum = models.CharField(max_length=100, null=True, blank=True)
    door_number= models.IntegerField(null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.owner)
    
    
class Family(models.Model):
    leader = models.OneToOneField(Resident, on_delete=models.CASCADE, null=True, blank=True)
    # hnum = models.IntegerField( null=True, blank=True)
    family_number= models.IntegerField(null=True, blank=True)
    male_number= models.IntegerField(null=True, blank=True)
    female_number= models.IntegerField(null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.leader)
    
    
class LocalBusiness(models.Model):
    owner = models.ForeignKey(Resident, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    type= models.CharField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.owner.first_name)
    

class IDCard(models.Model):
    resident = models.OneToOneField(Resident, on_delete=models.CASCADE, null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.resident.first_name)
    
    
class KebeleLand(models.Model):
    location = models.CharField(max_length=500, null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.location)
    
class KebeleHouse(models.Model):
    hnum = models.CharField(max_length=100, null=True, blank=True)
    door_number= models.IntegerField(null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.location)