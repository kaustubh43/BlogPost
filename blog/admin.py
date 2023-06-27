from django.contrib import admin

from . import models

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    """To show limited fields in admin end point"""
    list_display = ('title', 'created', 'author')

admin.site.register(models.Blog, BlogAdmin)
