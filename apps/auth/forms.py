from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import SEUser


class SignupForm(UserCreationForm):
    class Meta:
        model = SEUser
        fields = ('email',)


class SingInForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)
