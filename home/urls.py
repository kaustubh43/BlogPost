from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeBlogView.as_view(), name='home'),
    
]