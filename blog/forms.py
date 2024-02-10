from django.forms import ModelForm

from .models import Blog, Comment


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog', 'status']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'star']

