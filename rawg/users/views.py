from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .models import CustomUser, GameList, GameListItem
from .forms import RegisterUserForm, GameListForm

class Login(LoginView):
    template_name = 'users/accounts/login.html'

class Logout(LogoutView):
    next_page = '/'

class RegisterUser(FormView):
    template_name = 'users/accounts/register.html'
    form_class = RegisterUserForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)