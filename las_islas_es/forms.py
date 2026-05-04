from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter your email'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].label = "Password"
        self.fields['password1'].widget.attrs['placeholder'] = "Enter your password"

        self.fields['password2'].label = "Confirm Password"
        self.fields['password2'].widget.attrs['placeholder'] = "Confirm your password"