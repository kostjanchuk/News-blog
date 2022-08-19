from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput({'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput({'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput({'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput({'class': 'form-control'}))


