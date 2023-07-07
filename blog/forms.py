from django import forms
from .models import Blog

class BlogForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'text', 'category')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control my-5 mx-auto', 
                'placeholder': 'Enter a title', 
                'style': 'max-width: 1200px;',
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control my-5 mx-auto',
                'placeholder': 'Enter the body of your blog', 
                'style': 'max-width: 1200px;',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control my-5 mx-auto', 
                'placeholder': 'Category', 
                'style': 'max-width: 800px;',
                'text-align': 'center',
            }),
        }
        labels = {
            'title': 'Title',
            'text': 'Body',
            'category': 'Category',
        }
