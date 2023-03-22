from django import forms
from .models import Post, Comments


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'blog_post')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass form-control'}),
            'blog_post': forms.Textarea(attrs={'class': 'editable medium-editor-textarea post-content form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass form-control'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea form-control'}),
        }
