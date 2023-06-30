# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Blog
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from .forms import BlogForms

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForms
    success_url = '/blogs/blog'
    login_url = '/admin'


# Create your views here.
def error_404_view(request, exception):
    # we add the path to the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')


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
    ordering = ['-created_date_time']
