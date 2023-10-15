from django.urls import path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('blog', views.BlogListView.as_view(), name='blog.list'),
    path('blog/<int:pk>', views.BlogDetialView.as_view(), name='blog.details'),
    path('blog/new', views.BlogCreateView.as_view(), name='blog.create'),
    path('blog/<int:pk>/edit', views.BlogUpdateView.as_view(), name='blog.edit'),
    path('blog/<int:pk>/delete', views.BlogDeleteView.as_view(), name='blog.delete'),
    path('blog/<int:pk>/accessdenied',views.AccessDenied.as_view(), name='blog.accessdenied'),
    path('blog/<int:blog_id>/addcomment', views.BlogComment.as_view(), name='blog.addcomment')

]

handler404 = 'blog.views.error_404_view'
