from django.urls import path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('blog',views.BlogListView.as_view(), name='blog.list'),
    path('blog/<int:pk>', views.BlogDetialView.as_view(), name='blog.details'),
    path('blog/new', views.BlogCreateView.as_view(),name='blog.create'),
]

handler404 = 'blog.views.error_404_view'
