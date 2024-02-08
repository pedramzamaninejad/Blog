from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views import generic

from .models import Blog
from .forms import BlogForm


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'


class BlogCreateView(generic.CreateView):
    form_class = BlogForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blog-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
