from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView

from .form import CustomUserCreationForm

class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')


class CustomLogoutView(LogoutView):
    http_method_names = ['post', 'get', 'options']
    template_name = 'registration/logout.html'

    def get_success_url(self):
        return reverse_lazy('blog:list')
