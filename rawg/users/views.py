from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from .models import CustomUser, GameList, GameListItem
from .forms import RegisterUserForm, GameListForm

class Login(LoginView):
    template_name = 'users/accounts/login.html'

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form, error_message="Error al loguear el usuario.")
        )

class Logout(LogoutView):
    next_page = '/'

class RegisterUser(FormView):
    template_name = 'users/accounts/register.html'
    form_class = RegisterUserForm
    success_url = '/'

    def form_valid(self, form):
        try:
            user = form.save()
            login(self.request, user)
            return super().form_valid(form)
        except Exception as e:
            return self.render_to_response(
                self.get_context_data(form=form, error_message=f"Error al registrar el usuario: {str(e)}")
            )
    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form, error_message="Error al registrar el usuario.")
        )