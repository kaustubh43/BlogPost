from django.contrib import admin

from . import models

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    """To show limited fields of blog table in admin end point"""
    list_display = ('title', 'created_at', 'author', 'category_name')
 
    
class CategoryAdmin(admin.ModelAdmin):
    """To show categories fields in admin end point"""
    list_display = ('name', 'created_at')


admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category, CategoryAdmin)
