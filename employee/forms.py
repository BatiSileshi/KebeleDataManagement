from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Employee, Profile, Message
from django import forms


class UserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['first_name','last_name', 'email', 'username', 'password1', 'password2']
        
        
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = {'user'}
        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
        




class KebeleEmployeeForm(ModelForm):
    class Meta:
        model= Employee
        fields = '__all__'
        
        
    def __init__(self, *args, **kwargs):
        super(KebeleEmployeeForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
    
     
    
class MessageForm(ModelForm):
    class Meta:
        model= Message
        fields =['recipient', 'subject', 'body']
        
        widgets = {
            'recipient': forms.CheckboxSelectMultiple()
        }
        
        

        
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            self.fields['recipient'].widget.attrs.update({'id': 'form-check-input'})
            
            self.fields['subject'].widget.attrs.update({'class': 'form-control'})
            self.fields['body'].widget.attrs.update({'class': 'form-control'})
        
