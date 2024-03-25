from django.forms import ModelForm
from django_ckeditor_5.widgets import CKEditor5Widget
from django import forms
from .models import Blog, Comment, CommentReply


class BlogForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["blog"].required = True

    class Meta:
        model = Blog
        fields = ['title', 'blog', 'status']
        widgets = {
            'blog': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5", "row": "20"}, config_name="extends"
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
