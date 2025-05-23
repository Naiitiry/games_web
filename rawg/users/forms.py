from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import CustomUser, GameList

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        
class GameListForm(ModelForm):
    class Meta:
        model = GameList
        fields = ('name',)
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
        }
