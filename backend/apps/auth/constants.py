from django.utils.translation import gettext as _


class Messages:
    INVALID_EMAIL = [
        {"message": _("The email address is invalid"), "code": "invalid_email"}]
    INVALID_CREDENTIALS = [{"message": _(
        "The email or password in is incorrect"), "code": "invalid_credentials"}]
    PASSWORD_DOESNOT_MATCH = [
        {"message": _("Password does not match"), "code": "password_does_not_match"}]
    EMAIL_IN_USE = [
        {"message": _("This email address already exists"), "code": "email_in_use"}]


class EMAIL_MESSAGES:
    SIGN_UP = {
        'subject': _("Sign up"),
        'template': 'activate_account_signup.html',
    }


class TokenAction(object):
    ACTIVATION = "activation"
    PASSWORD_RESET = "password_reset"
    ACTIVATION_SECONDARY_EMAIL = "activation_secondary_email"
    PASSWORD_SET = "password_set"
