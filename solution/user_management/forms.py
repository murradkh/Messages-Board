from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {'username': forms.TextInput(attrs={
            "placeholder": "Username"
        }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Email"
            }),
            "password": forms.PasswordInput(attrs={'placeholder': 'Password'})

        }
