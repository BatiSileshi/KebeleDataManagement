from django.forms import ModelForm, widgets
from django import forms
from .models import Resident

class ResidentForm(ModelForm):
    class Meta:
        model= Resident
        fields = '__all__'
        
        # labels = {
        #     'first_name': 'Maqaa',
        #     'last_name': 'Maqaa Abbaa',
        #     'email': 'Imeeyilii',
        #     'username': 'Maqaa fayyadamaa',
        #     'password1': 'Jecha darbii',
        #     'password2': 'Jecha darbii mirkaneessaa',
        # }
        
    # def __init__(self, *args, **kwargs):
    #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})