from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, generic.TemplateView):
    model = CustomUser
    template_name = 'account/profile.html'
    http_method_names = ['get', 'options']

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['user'] = CustomUser.objects.get(id=self.request.user.id)

        print(context['user'].first_name)

        return context
