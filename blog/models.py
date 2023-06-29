from django.db import models

# Create your models here.


class Category(models.Model):
    """Model for a Category"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Blog(models.Model):
    """Model for a Single Blog"""
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField(default=' ')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    author = models.CharField(max_length=75)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    @property
    def category_name(self):
        return self.category.name