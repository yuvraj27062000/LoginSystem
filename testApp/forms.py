from django.contrib.auth.models import User
from django import forms

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','password','email','first_name','last_name']


def clean_name(self): 
    fp=self.cleaned_data['Password']
    sp=self.cleaned_data['Re_password'] 
    if fp != sp :
        raise forms.ValidationError(' Password Should be matched')
    p = True 
    return p


    
