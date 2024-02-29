from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget

from .models import Blog, Comment, CommentReply


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'blog', 'status']
        widgets = {
            'blog': CKEditorWidget()
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'star']


class CommentReplyForm(ModelForm):
    class Meta:
        model = CommentReply
        fields = ['body']
