from django.shortcuts import render, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Blog, Comment
from .forms import BlogForm, CommentForm


class BlogListView(generic.ListView):
    # model = BlogListView
    queryset = Blog.objects.filter(status='Pub').all()
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'


class BlogDetailView(generic.DetailView):
    # model = Blog
    queryset = Blog.objects.prefetch_related('comments').all()
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['comment_form'] = CommentForm()
        return context


class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = BlogForm
    template_name = 'blog/blog_create.html'
    success_url = reverse_lazy('blog:list')

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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Blog
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:list')

    def test_func(self):
        blog_user = self.get_object().author
        return blog_user == self.request.user


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user

        blog_id = int(self.kwargs['id'])
        blog = get_object_or_404(Blog, blog_id)
        obj.blog = blog
        
        return super().form_valid(form)


@login_required()
def personal_blog(request):
    query = Blog.objects.filter(author_id=request.user.id)

    context = {
        "blogs": query
    }

    return render(request, 'blog/blog_list.html', context=context)
