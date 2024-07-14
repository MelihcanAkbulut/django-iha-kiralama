from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms

from . import models

# - Register/Create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = models.UserProfile
        fields = ('email', 'username', 'password1', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = models.UserProfile
        fields = ('username', 'password')

# - Login a user

class LoginForm(AuthenticationForm):

    name = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
