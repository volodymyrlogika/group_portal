from django.conf.urls import handler403
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import UserLoginForm, UserRegisterForm
from accounts.models import UserProfile, Role


# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    form_class = UserLoginForm

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')

class RegisterView(CreateView):
    template_name = 'accounts/register.html'
    form_class = UserRegisterForm
    success_url = 'accounts:login'

    def form_valid(self, form):
        user = form.save()
        default_role, created = Role.objects.get_or_create(name = 'User')
        UserProfile.objects.create(user = user, role=default_role)
        login(self.request, user)
        return redirect(reverse_lazy('accounts:login'))


def custom_403_view(request, exception=None):
    return render(
        request, "403.html", {"message": "Особливе повідомлення!"}, status=403
    )