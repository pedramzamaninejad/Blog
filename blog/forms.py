from django.forms import ModelForm
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from .models import Blog, Comment, CommentReply


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog', 'status']
        widgets = {
            'blog': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'star']


class CommentReplyForm(ModelForm):
    class Meta:
        model = CommentReply
        fields = ['body']
