# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog

# Create your views here.



class BlogDetialView(DetailView):
    """View Blog Details of single Blog"""
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_details.html'


class BlogListView(ListView):
    """View blog Details of all Blogs"""
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'
