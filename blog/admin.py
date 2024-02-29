from django.contrib import admin

from .models import Blog, Comment, CommentReply

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


class CommentReplyInline(admin.TabularInline):
    model = CommentReply
    extra = 1


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    inlines = [CommentInline,]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'blog', 'star']
    inlines = [CommentReplyInline,]


@admin.register(CommentReply)
class CommentReplyAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at']
