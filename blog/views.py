# from django.shortcuts import render
from typing import Any
from django.forms.widgets import HiddenInput
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Blog, Comment
from django.http.response import HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render
from .forms import BlogForms, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse


class AccessDenied(TemplateView):
    template_name = 'blog/denied.html'


class BlogComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    # success_url = '/blogs/blog'
    template_name = 'blog/blog_add_comment.html'
    login_url = '/login'

    def form_valid(self, form):
        # Set the author to the currently logged-in user
        form.instance.author = self.request.user
        blog_id = self.kwargs.get('blog_id')
        blog = get_object_or_404(Blog, pk=blog_id)
        form.instance.blog = blog
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog.details', args=[self.object.blog_id])


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
