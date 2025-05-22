from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import CustomUser, GameList

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class GameListForm(ModelForm):
    class Meta:
        model = GameList
        field = ('name',)
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
        }
