from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from .forms import ProfileForm
from guns.tasks import send_welcome_email
from django.http import JsonResponse
from .models import User

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


def register_user(request):
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")

    if not username or not email or not password:
        return JsonResponse({"error": "Missing fields!"}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)


    if email.endswith("@staff.com"):
        user.is_staff = True
        user.save()


    send_welcome_email.delay(email)

    return JsonResponse({"message": "User registered!", "is_moderator": user.is_staff})