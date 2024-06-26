from django import forms
from django.contrib.auth.models import User
from .models import Post



class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'caption']
        widgets = {
            'caption': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'title': 'Title',
            'image': 'Image',
            'caption': 'Caption',
        }