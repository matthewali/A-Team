from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class CreateRatingForm(forms.ModelForm):
    class Meta:
        model = BookRating
        fields = [
            'title',
            'book',
            'num_stars',
            'comment',
        ]

