from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Blog, Comment, CommentReply


class BlogForm(ModelForm):
    blog = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = ['title', 'blog', 'status']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'star']


class CommentReplyForm(ModelForm):
    class Meta:
        model = CommentReply
        fields = ['body']
