from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import *
from authorization.forms import UserForm
from authorization.models import User


class RegisterCreateView(CreateView):
    model = User
    template_name = "login/register.html"
    form_class = UserForm
    success_url = "/login"


class Login(LoginView):
    template_name = 'login/login.html'


class Logout(LogoutView):
    def get(self, request, **kwargs):
        logout(request)


@login_required(login_url='login')
def UserPage(request):
    return render(request, 'login/profile.html')
