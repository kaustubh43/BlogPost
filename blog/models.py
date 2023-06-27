from django.db import models

# Create your models here.
class Blog(models.Model):
    """Model for a Single Blog"""
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField(default=' ')
    created = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=75)
