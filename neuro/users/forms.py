from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField

class UserRegisterForm(UserCreationForm):
    login = forms.CharField(widget=forms.UsernameField(attr={'class':'un'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attr={'class':'pass'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attr={'class':'pass'}))
    email = forms.EmailField(widget=forms.EmailInput(attr={'class':'un'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']