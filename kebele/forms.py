from django.forms import ModelForm, widgets
from django import forms
from .models import Resident, LocalBusiness, Address, House, Family, IDCard, KebeleHouse, KebeleLand, BusinessOwner

class ResidentForm(ModelForm):
    class Meta:
        model= Resident
        fields = '__all__' 
        
        labels = {
            'kebele': 'Ganda',
            'first_name': 'Maqaa',
            'middle_name': 'Maqaa Abba',
            'last_name': 'Maqaa Akaakayyuu',
            'mother_name': 'Maqaa Haadhaa',
            'photo': 'Suuraa',
            'phone_number': 'Bilbila',
            'first_name': 'Maqaa',
            'email': 'Imeeyilii',
            'age': 'Umurii',
            'sex': 'Saala',
            'edu_level': 'Sadarkaa Barnootaa',
            'nationality': 'Lammummaa',
            'religion': 'Amantii',
            'occupation': 'Hojii',
            'is_here': 'As jiraata',

        }
        
    # def __init__(self, *args, **kwargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})
    
    

        

class AddressForm(ModelForm):
    class Meta:
        model= Address
        exclude = ['resident'] 
        
        labels = {
            'hnum': 'Lakk Manaa ',
            'gooxii': 'Gooxii',
            'garee': 'Garee',

        }
        
class HouseForm(ModelForm):
    class Meta:
        model= House
        fields = '__all__'
        
        labels = {
            'owner': 'Abbaa qabeenyaa',
            'hnum': 'Lakk Manaa ',
            'door_number': 'Baayyina balbalaa',
            'area': 'Ballina',
        }
        
        
class FamilyForm(ModelForm):
    class Meta:
        model= Family
        fields = '__all__'
        
        labels = {
            'leader': 'Geggeessaa Maatii',
            'members': 'Miseensota Maatii',
            'house': 'Mana',
            'family_number': 'Baayyina Maatii',
            'male_number': 'Baayyina Dhiiraa',
            'female_number': 'Baayyina Dhalaa',
        }
        
        
class IDCardForm(ModelForm):
    class Meta:
        model= IDCard
        fields = '__all__'
        
        labels = {
            'resident': 'Jiraataa',
            'id_number': 'Lakk Eenyummeessaa',

        }
        


class BusinessOwnerForm(ModelForm):
    class Meta:
        model = BusinessOwner
        fields = '__all__'
        
        labels = {
            'name': 'Maqaa',
            'phone_number': 'Bilbila',
        }  
        
        
class LocalBusinessForm(ModelForm):
    class Meta:
        model= LocalBusiness
        fields = '__all__'
        
        labels = {
            'owner': 'Abbaa Qabeenyaa',
            'name': 'Daldala',
            'type': 'Gosa ',
        }
        
        
class KebeleHouseForm(ModelForm):
    class Meta:
        model= KebeleHouse
        fields = '__all__'
        
        labels = {
            'hnum': 'Lakk Manaa',
            'door_number': 'Baayyina balbalaa',
            'location': 'Bakka argamaa',
            'area': 'Ballina',

        }
        
        
class KebeleLandForm(ModelForm):
    class Meta:
        model= KebeleLand
        fields = '__all__'
        
        labels = {
            'location': 'Bakka argamaa',
            'area': 'Ballina',

        }