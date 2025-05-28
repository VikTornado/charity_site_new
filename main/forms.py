from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Contact form for ContactMessage model
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded px-3 py-2', 'placeholder': "Ваше ім'я"}),
            'email': forms.EmailInput(attrs={'class': 'w-full border rounded px-3 py-2', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'w-full border rounded px-3 py-2', 'placeholder': 'Ваше повідомлення'}),
        }