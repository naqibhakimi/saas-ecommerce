from django.contrib.auth.forms import (UserCreationForm)


from .models import SEUser


class SignupForm(UserCreationForm):
    class Meta:
        model = SEUser
        fields = ('email',)