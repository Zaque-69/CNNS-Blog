from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta :
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class UpdateUser(forms.ModelForm):
    
    email = forms.EmailField()
    class Meta : 
        model = User
        fields = ['username', 'email'] 

class UpdateUserAfterClass(forms.ModelForm):
    last_name = forms.CharField(max_length=100)
    class Meta : 
        model = User
        fields = ['last_name'] 
