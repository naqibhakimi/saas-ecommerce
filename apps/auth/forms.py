from django.contrib.auth.forms import (UserCreationForm)
from django import forms


from .models import SEUser


class SignupForm(UserCreationForm):
    class Meta:
        model = SEUser
        fields = ('email',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
