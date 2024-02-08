from django.urls import path

from .views import BlogListView, BlogCreateView, BlogUpdateView

app_name = 'blog'

urlpatterns = [
    path('list/', BlogListView.as_view(), name='blog-list'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('<int:pk>', BlogUpdateView.as_view(), name='blog-update'),
]
