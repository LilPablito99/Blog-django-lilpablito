from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Perfil

class SignUpForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'contraseña', 'style': 'width: 300px;', 'class': 'input'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'repetir contraseña', 'style': 'width: 300px;', 'class': 'input'}))

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            
        )
        widgets={
            'username':forms.TextInput(attrs={'placeholder': 'Usuario', 'style': 'width: 300px;', 'class': 'input'}),
            'email':forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'input'}),
        }