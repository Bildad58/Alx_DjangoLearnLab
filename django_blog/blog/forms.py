from django import forms
from .models import Post, Comment

from taggit.forms import TagField  

class PostForm(forms.ModelForm):
    tags ="TagWidget()"

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),  
        }


class CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = ['content']


