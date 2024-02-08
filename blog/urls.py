from django.urls import path

from .views import BlogListView

app_name = 'blog'

urlpatterns = [
    path('list', BlogListView.as_view(), name='blog-list'),
]
