from django.forms import ModelForm, widgets
from django import forms
from .models import Resident, LocalBusiness, Address, House, Family, IDCard, KebeleHouse, KebeleLand

class ResidentForm(ModelForm):
    class Meta:
        model= Resident
        fields = '__all__'
        
        labels = {
            'first_name': 'Maqaa',
            'last_name': 'Maqaa Abbaa',
            'email': 'Imeeyilii',
            'username': 'Maqaa fayyadamaa',
            'password1': 'Jecha darbii',
            'password2': 'Jecha darbii mirkaneessaa',
        }
        
    # def __init__(self, *args, **kwargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})
    
    
class LocalBusinessForm(ModelForm):
    class Meta:
        model= LocalBusiness
        fields = '__all__'
        
        labels = {
            'owner': 'Abbaa Qabeenyaa',
            'name': 'Daldala',
            'type': 'Gosa ',
            'quantity': 'Baayyina',
        }
        

class AddressForm(ModelForm):
    class Meta:
        model= Address
        exclude = ['resident'] 
        
        labels = {
            'phone_number': 'Lakk bilbilaa',
            'email': 'Imeeyilii ',
            'hnum': 'Lakk Manaa ',
            'kebele': 'Ganda',
            'city': 'Magaalaa',
            'zone': 'Godina',
            'region': 'Naannoo',
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