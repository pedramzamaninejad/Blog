from django.urls import path
from django.views.generic import TemplateView

from .views import RegisterView, ProfileView

app_name = 'account'

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signout/', TemplateView.as_view(template_name='registration/logout.html'), name='signout'),
    path('profile/', ProfileView.as_view(), name='profile')
]
