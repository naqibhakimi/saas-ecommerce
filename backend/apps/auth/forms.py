from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', "first_name", "last_name")


class SingInForm(forms.Form):
    email = forms.EmailField(max_length=100, required=True)
    password = forms.CharField(max_length=100, required=True)


class EmailForm(forms.Form):
    email = forms.EmailField(max_length=100)
