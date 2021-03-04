from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Register(UserCreationForm):
    class Meta: 
        model = User
        fields = [
            'username', 'email'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full border-b border-green-400 py-1 my-2 px-3 focus:outline-none', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'w-full border-b border-green-400 py-1 my-2 px-3 focus:outline-none', 'placeholder': 'E-mail'}),
            'password': forms.TextInput(attrs={'class': 'w-full border-b border-green-400 py-1 my-2 px-3 focus:outline-none', 'placeholder': 'Password'}),
            'Password confirmation': forms.TextInput(attrs={'class': 'w-full border-b border-green-400 py-1 my-2 px-3 focus:outline-none', 'placeholder': 'Confirm'}),
        }
        

