from django.urls import path

from . import views

urlpatterns = [
    path('blog',views.BlogListView.as_view(), name='blog.list'),
    path('blog/<int:pk>', views.BlogDetialView.as_view(), name='blog.details'),
]