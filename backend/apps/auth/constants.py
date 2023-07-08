from django.utils.translation import gettext as _


class Messages:
    ALREADY_VERIFIED = [
        {"message": _("The user already verified"), "code": "user_already_verified"}
    ]
    EXPIRED_TOKEN = [
        {"message": _("The provided token is invalid"), "code": "invalid_token"}
    ]
    INVALID_TOKEN = [
        {"message": _("The provided token is invalid"), "code": "invalid_token"}
    ]
    INVALID_EMAIL = [
        {"message": _("The email address is invalid"), "code": "invalid_email"}
    ]
    INVALID_CREDENTIALS = [
        {
            "message": _("The email or password in is incorrect"),
            "code": "invalid_credentials",
        }
    ]
    PASSWORD_DOESNOT_MATCH = [
        {"message": _("Password does not match"), "code": "password_does_not_match"}
    ]
    EMAIL_IN_USE = [
        {"message": _("This email address already exists"), "code": "email_in_use"}
    ]

    EMAIL_FAIL = [
        {"message": _("An error occurred while sending the email, SMTPException problem ")}
    ]

    NOT_VERIFIED_PASSWORD_RESET = [
        {"message": _("your email is not verified to rest the password")}
    ]


class EMAIL_MESSAGES:
    SIGN_UP = {
        "subject": _("Sign up"),
        "template": "email/activation_email.html",
    }


class TokenAction(object):
    ACTIVATION = "activation"
    PASSWORD_RESET = "password_reset"
    ACTIVATION_SECONDARY_EMAIL = "activation_secondary_email"
    PASSWORD_SET = "password_set"
