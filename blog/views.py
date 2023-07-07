# from django.shortcuts import render
from typing import Any
from django.forms.widgets import HiddenInput
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Blog
from django.http.response import HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render
from .forms import BlogForms
from django.contrib.auth.mixins import LoginRequiredMixin


class AccessDenied(TemplateView):
    template_name = 'blog/denied.html'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blogs/blog'
    template_name = 'blog/blog_delete.html'


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect('accessdenied') 



class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForms
    success_url = '/blogs/blog'
    template_name = 'blog/blog_form_edit.html'
    login_url = '/login'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        if self.object.author == self.request.user:
            self.object.save()
            return HttpResponseRedirect(self.get_success_url())
        else: 
            return HttpResponseRedirect('accessdenied')


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForms
    success_url = '/blogs/blog'
    login_url = '/login'
    template_name = 'blog/blog_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


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
