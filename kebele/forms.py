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


        }
        
    def __init__(self, *args, **kwargs):
        super(ResidentForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
    
    

        

class AddressForm(ModelForm):
    class Meta:
        model= Address
        exclude = ['resident'] 
        
        labels = {
            'hnum': 'Lakk Manaa ',
            'gooxii': 'Gooxii',
            'garee': 'Garee',

        }
        
    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            
            
        
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
        
    def __init__(self, *args, **kwargs):
        super(HouseForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
        
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
        widgets = {
            'members': forms.CheckboxSelectMultiple(),
            'house': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(FamilyForm, self).__init__(*args, **kwargs)
        self.fields['leader'].widget.attrs.update({'class': 'form-control'})
        self.fields['members'].widget.attrs.update({'id': 'form-check-input'})
        self.fields['house'].widget.attrs.update({'id': 'form-check-input'})
        self.fields['family_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['male_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['female_number'].widget.attrs.update({'class': 'form-control'})
        
        
class IDCardForm(ModelForm):
    class Meta:
        model= IDCard
        fields = '__all__'
        
        labels = {
            'resident': 'Jiraataa',
            'id_number': 'Lakk Eenyummeessaa',

        }
        
    def __init__(self, *args, **kwargs):
        super(IDCardForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class BusinessOwnerForm(ModelForm):
    class Meta:
        model = BusinessOwner
        fields = '__all__'
        
        labels = {
            'name': 'Maqaa',
            'phone_number': 'Bilbila',
        }  
        
    def __init__(self, *args, **kwargs):
        super(BusinessOwnerForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
class LocalBusinessForm(ModelForm):
    class Meta:
        model= LocalBusiness
        fields = '__all__'
        
        labels = {
            'owner': 'Abbaa Qabeenyaa',
            'name': 'Daldala',
            'type': 'Gosa ',
        }
        
    def __init__(self, *args, **kwargs):
        super(LocalBusinessForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
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
        
    def __init__(self, *args, **kwargs):
        super(KebeleHouseForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
        
class KebeleLandForm(ModelForm):
    class Meta:
        model= KebeleLand
        fields = '__all__'
        
        labels = {
            'location': 'Bakka argamaa',
            'area': 'Ballina',

        }
        
    def __init__(self, *args, **kwargs):
        super(KebeleLandForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})