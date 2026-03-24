from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'users/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile