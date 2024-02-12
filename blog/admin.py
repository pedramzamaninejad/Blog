from django.contrib import admin

from .models import Blog, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    inlines = [CommentInline,]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'blog', 'star']
