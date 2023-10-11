from django.contrib import admin

from . import models


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    """To show limited fields of blog table in admin end point"""
    list_display = ('title', 'created_at', 'author', 'category_name')

    def display_comments(obj):
        # Get a list of comment texts related to this blog.
        comments = models.Comment.objects.filter(blog_id=obj)
        return ', '.join(comment.text for comment in comments)

    
class CategoryAdmin(admin.ModelAdmin):
    """To show categories fields in admin end point"""
    list_display = ('name', 'created_at')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'author', 'text')


admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Comment, CommentAdmin)
