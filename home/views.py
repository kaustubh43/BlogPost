from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from blog.models import Blog,Category
from django.views.generic import ListView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm


class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/blogs/blog'


class LogoutInterfaceView(LogoutView):
    "Login Inteface"
    template_name = 'home/logout.html'


class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'
    success_url = 'blogs/blog'


class HomeBlogView(ListView):
    model = Blog
    template_name = 'home/welcome.html'
    context_object_name = 'latest_posts'
    ordering = ['-created_date_time']
    paginate_by = 5


# Not used remove later
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
