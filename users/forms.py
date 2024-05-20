from django import forms
from .models import Profile

class ProfileIconForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'background', 'website', 'description']