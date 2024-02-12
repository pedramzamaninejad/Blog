from django.urls import path

from .views import BlogListView, BlogCreateView, BlogUpdateView, BlogDetailView, CommentCreateView, BlogDeleteView, \
    personal_blog

app_name = 'blog'

urlpatterns = [
    path('list/', BlogListView.as_view(), name='list'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('personal/', personal_blog, name='personal'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/edit', BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='delete'),
    path('<int:id>/comment', CommentCreateView.as_view(), name='comment'),
]
