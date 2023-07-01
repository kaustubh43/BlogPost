# from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from .forms import BlogForms

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blogs/blog'
    template_name = 'blog/blog_delete.html'



class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForms
    success_url = '/blogs/blog'
    template_name = 'blog/blog_form_edit.html'


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForms
    success_url = '/blogs/blog'
    login_url = '/admin'
    template_name = 'blog/blog_form.html'


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
