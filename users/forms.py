from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

        labels = {
            'bio': 'Your Bio',
            'profile_picture': 'Profile Image',
        }

        help_texts = {
            'bio': 'Tell something about yourself',
        }

        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write something about yourself...'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }