from django.forms import ModelForm, widgets
from django import forms
from .models import Resident, LocalBusiness, Address, House, Family, IDCard, BirthCertificate, KebeleHouse,  BusinessOwner

class ResidentForm(ModelForm):
    class Meta:
        model= Resident
        exclude=['kebele']
        
        
    def __init__(self, *args, **kwargs):
        super(ResidentForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
               

class AddressForm(ModelForm):
    class Meta:
        model= Address
        exclude = ['resident'] 
        
        labels = {
            'hnum': 'Lives in ',
            'gooxii': 'Local community',
            'garee': 'Group',

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
            'hnum': 'House number ',
        }
        
    def __init__(self, *args, **kwargs):
        super(HouseForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
        
class FamilyForm(ModelForm):
    class Meta:
        model= Family
        fields = '__all__'


        widgets = {
            'members': forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(FamilyForm, self).__init__(*args, **kwargs)
        self.fields['leader'].widget.attrs.update({'class': 'form-control'})
        self.fields['members'].widget.attrs.update({'id': 'form-check-input'})
        self.fields['family_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['male_number'].widget.attrs.update({'class': 'form-control'})
        self.fields['female_number'].widget.attrs.update({'class': 'form-control'})
        
        
class IDCardForm(ModelForm):
    class Meta:
        model= IDCard
        fields = '__all__'
        

        
    def __init__(self, *args, **kwargs):
        super(IDCardForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class BusinessOwnerForm(ModelForm):
    class Meta:
        model = BusinessOwner
        fields = '__all__'
        

        
    def __init__(self, *args, **kwargs):
        super(BusinessOwnerForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
class LocalBusinessForm(ModelForm):
    class Meta:
        model= LocalBusiness
        fields = '__all__'
        

        
    def __init__(self, *args, **kwargs):
        super(LocalBusinessForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
class KebeleHouseForm(ModelForm):
    class Meta:
        model= KebeleHouse
        fields = '__all__'
        
        labels = {
            'hnum': 'House number',

        }
        
    def __init__(self, *args, **kwargs):
        super(KebeleHouseForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
        
        
class BirthCertificateForm(ModelForm):
    class Meta:
        model= BirthCertificate
        fields = '__all__'

        
    def __init__(self, *args, **kwargs):
        super(BirthCertificateForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        
