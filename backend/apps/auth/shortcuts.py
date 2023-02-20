from .models import SEUser, UserStatus
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

# UserModel = get_user_model
UserModel = SEUser


def get_user_by_email(email):
    try:
        return UserModel._default_manager.get(**{UserModel.EMAIL_FIELD: email})
    except ObjectDoesNotExist:
        status = UserStatus._default_manager.get(secondary_email=email)
        return status.user
