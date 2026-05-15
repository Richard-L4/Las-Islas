from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from .models import Contact, Comment

class RegisterForm(UserCreationForm):
    
    username = forms.CharField(
        label="Username",
        help_text="3–20 characters. Letters, numbers, underscores only.",
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_]{3,20}$',
                message="Username must be 3–20 characters. Letters, numbers and underscores only."
            )
        ],
        widget=forms.TextInput(attrs={'placeholder': 'e.g. john_doe123'})
    )

    email = forms.EmailField(
        label="Email Address",
        help_text="Enter a valid email address.",
        widget=forms.EmailInput(attrs={'placeholder': 'e.g. john@example.com'})
    )

    password1 = forms.CharField(
        label="Password",
        help_text="At least 8 characters, one uppercase, one lowercase, one number.",
        validators=[
            RegexValidator(
                regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$',
                message="Password must be at least 8 characters and include one uppercase letter, one lowercase letter, and one number."
            )
        ],
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

    password2 = forms.CharField(
        label="Confirm Password",
        help_text="Enter the same password again.",
        widget=forms.PasswordInput(attrs={'placeholder': 'Re-enter your password'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    name = forms.CharField(max_length=20,
                           label="Username",
                           widget=forms.TextInput(
                               attrs={'placeholder': 'Enter username'}
                           ))
    
    password = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your password'}
    ))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        labels = {
            'name': 'Full name',
            'email': 'Email',
            'phone': 'Phone',
            'message': 'Message',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Enter your name'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Enter your email'}
            ),
            'phone': forms.TextInput(
                attrs={'placeholder': 'Enter your phone number'}
            ),
            'message': forms.Textarea(
                attrs={'placeholder': 'Enter your message'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': '',
        }
        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control',
                       'rows': 3,
                       'placeholder': 'Enter your comment here'}
            )
        }