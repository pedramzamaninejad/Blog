from django.urls import path

from .views import BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, CommentCreateView

app_name = 'blog'

urlpatterns = [
    path('list/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', BlogUpdateView.as_view(), name='update'),
    path('comment/<int:id>', CommentCreateView.as_view(), name='comment'),
]
