from django.db import models

# Create your models here.
from django.contrib.gis.db import models


class Kebele(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    woreda = models.CharField(max_length=200, null=True, blank=True)
    zone = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name
    

class Resident(models.Model):
    SAALA=(
        ('Male', 'Male'),
        ('Female', 'Female'),    
    )
    
    EDUCATION_LEVEL=(
        ('elementary', 'Elementary'),
        ('hight_school', 'High School'),    
        ('diploma', 'Diploma'),    
        ('degree', 'Degree'),    
        ('masters', 'Masters'),    
        ('phd', 'PHD'),    
    )
    
    OCCUPATION=(
        ('teacher', 'Teacher'),
        ('merchant', 'Merchant'),    
        ('office_worker', 'Office Worker'),    
        ('nurse', 'Nurse'),    
        ('doctor', 'Doctor'),    
        ('student', 'Student'),   
        ('other', 'Other'),  
        ('none', 'None'),   
    )
    kebele = models.ForeignKey(Kebele, on_delete=models.SET_NULL, null=True, blank=True )
    first_name=models.CharField(max_length=100, null=True, blank=True)
    middle_name=models.CharField(max_length=100, null=True, blank=True)
    last_name=models.CharField(max_length=100, null=True, blank=True)
    mother_name=models.CharField(max_length=100, null=True, blank=True)
    photo=models.ImageField(null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=20, null=True, blank=True, choices=SAALA)
    edu_level = models.CharField(max_length=200, null=True, blank=True, choices=EDUCATION_LEVEL)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    religion = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True, choices=OCCUPATION)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str((self.id, self.first_name, self.middle_name))
    class Meta:
        ordering = ['first_name']
    
    
class Address(models.Model):
    resident = models.OneToOneField(Resident, on_delete=models.CASCADE, null=True, blank=True)
    hnum = models.ForeignKey('House', on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.CharField(max_length=100, null=True, blank=True)
    gooxii = models.CharField(max_length=100, null=True, blank=True)
    garee = models.CharField(max_length=100, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.resident)
    class Meta:
        ordering = ['resident']
        
        
class IDCard(models.Model):
    resident = models.OneToOneField(Resident, on_delete=models.CASCADE, null=True, blank=True)
    emergency = models.CharField(max_length=200, null=True, blank=True)
    emergency_contact= models.IntegerField(null=True, blank=True)
    id_number = models.CharField(max_length=20, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.resident)
        

class House(models.Model):
    owner = models.OneToOneField(Resident, on_delete=models.CASCADE, null=True, blank=True)
    hnum = models.CharField(max_length=100, null=True, blank=True)
    door_number= models.IntegerField(null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.hnum)
    
        
class Family(models.Model):
    leader = models.ForeignKey(Resident, on_delete=models.CASCADE, null=True, blank=True)
    members = models.ManyToManyField(Resident, related_name="family_members")
    family_number= models.IntegerField(null=True, blank=True)
    male_number= models.IntegerField(null=True, blank=True)
    female_number= models.IntegerField(null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.leader)
    
    
    
    
    
   ################################################### 
   
class BusinessOwner(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.name)
    
   
class LocalBusiness(models.Model):
    owner = models.ForeignKey(BusinessOwner, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    type= models.CharField(max_length=100, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.owner.name)
    

 

    
    
class KebeleHouse(models.Model):
    hnum = models.CharField(max_length=100, null=True, blank=True)
    door_number= models.IntegerField(null=True, blank=True)
    area = models.CharField(max_length=100, null=True, blank=True)
    resident = models.OneToOneField(Resident,on_delete=models.SET_NULL,null=True,blank=True)
    location = models.PointField(null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.hnum)
    

    @property   
    def lat_lng(self): 
      return list(getattr(self.location,'coords',[])[::-1])
                
                
                
class BirthCertificate(models.Model):
    SAALA=(
        ('Male', 'Male'),
        ('Female', 'Female'),    
    )
    child = models.CharField(max_length=100, null=True, blank=True)
    birth_registration_number = models.BigIntegerField(null=True, blank=True)
    birth_unique_number = models.BigIntegerField(null=True, blank=True)
    father = models.ForeignKey(Resident, on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'sex': 'Male'})
    mother = models.ForeignKey(Resident, on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'sex': 'Female'}, related_name="mother")
    sex = models.CharField(max_length=20, null=True, blank=True, choices=SAALA)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    updated=models.DateTimeField(auto_now=True, null=True)
    created=models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.child)
    
    