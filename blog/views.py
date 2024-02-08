from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Blog
from .forms import BlogForm


class BlogListView(generic.ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'


class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = BlogForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:blog-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Blog
    fields = ['title', 'blog', 'status']
    template_name = 'blog/blog_update.html'

    def test_func(self):
        blog_user = self.get_object().author
        return blog_user == self.request.user
