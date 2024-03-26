from django.urls import path

from .views import RegisterView, CustomLogoutView

app_name = 'account'

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('signout/', CustomLogoutView.as_view(), name='logout'),
]
