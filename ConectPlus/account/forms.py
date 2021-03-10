from django import forms
from django.forms import fields
from .models import Profile
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput,
                    required=True)

class UserEditForm(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('date_of_birth', 'photo')