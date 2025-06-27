from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # Custom validation methods  - clean_<fieldname> is used to validate specific fields
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address already exists.")
        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == "root":
            raise forms.ValidationError("Username 'root' is not allowed.")
        
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists.")
        return username