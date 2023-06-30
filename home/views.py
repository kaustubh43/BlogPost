from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from blog.models import Blog,Category
from django.views.generic import ListView


# Create your views here.


class HomeBlogView(ListView):
    model = Blog
    template_name = 'home/welcome.html'
    context_object_name = 'latest_posts'
    ordering = ['-created_date_time']
    paginate_by = 5

# Not used remove later
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
