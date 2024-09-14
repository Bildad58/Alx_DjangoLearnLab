from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False)
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    class meta:
        model = Comment
        fields = ['content']


