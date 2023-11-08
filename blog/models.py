from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    """Model for a Category"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    """Model for a Single Blog"""
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField(default=' ')
    created_at = models.DateField(auto_now_add=True)
    created_date_time = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    @property
    def category_name(self):
        return self.category.name


class Comment(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.text
