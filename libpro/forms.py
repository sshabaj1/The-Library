from django import forms
from django.forms import widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title Tag'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Whats in your mind'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title', 'title_tag', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Post Title Tag'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Whats in your mind'}),
        }