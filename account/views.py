from django.views import generic
from django.urls import reverse_lazy

from .form import CustomUserCreationForm

class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')
