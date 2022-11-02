from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Task
from django.contrib.auth import get_user_model
User = get_user_model()


class createtask(forms.ModelForm):
    class Meta:
        model =  Task
        fields ="__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','password1','password2']