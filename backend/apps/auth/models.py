import time

from apps.core.models import BaseModel
from django.conf import settings
from django.conf import settings as django_settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.db import models
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
# from graphql_jwt.shortcuts import get_token

from .constants import TokenAction
from .exceptions import UserAlreadyVerified
from .signals import user_verified

from graphql_jwt.shortcuts import  get_token, get_user_by_token

class Oauth(BaseModel):
    display_name = models.CharField(max_length=255)
    application_name = models.CharField(max_length=255, unique=True)
    install_url = models.CharField(max_length=255, null=True)
    uninstall_url = models.CharField(max_length=255, null=True)
    data = models.JSONField(null=True)


class PublishableApiKeySalesChannel(BaseModel):
    sales_channel_id = models.CharField(max_length=100, unique=True)
    publishable_key_id = models.CharField(max_length=100, unique=True)


class PublishableApiKey(BaseModel):
    created_by = models.CharField(max_length=100, null=True)
    revoked_by = models.CharField(max_length=100, null=True)
    revoked_at = models.DateTimeField(null=True)
    title = models.CharField(max_length=100)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class SEUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return f'{self.pk}  {self.last_name} {self.first_name} {self.email}'

    def __repr__(self):
        return f'{self.pk}  {self.last_name} {self.first_name} {self.email}'

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)


class UserStatus(BaseModel):
    """
    A helper model that handles user account stuff.
    """

    user = models.OneToOneField(
        django_settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="status"
    )
    verified = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    secondary_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} - status"

    def send(self, subject, template, context, recipient_list=None):
        print(template)
        # _subject = render_to_string(subject, context).replace("\n", " ").strip()
        html_message = render_to_string(template, context)
        message = strip_tags(html_message)

        return send_mail(
            subject= subject,
            from_email=settings.AUTH.EMAIL_FROM,
            message=message,
            html_message=html_message,
            recipient_list=(
                recipient_list or [getattr(self.user, SEUser.EMAIL_FIELD)]
            ),
            fail_silently=False,
        )

    def get_email_context(self, info, path, action, **kwargs):
        token = get_token(self.user, action, **kwargs)
        site = get_current_site(info.context)
        origin = info.context.headers.get('Origin', False)

        return {
            "user": self.user,
            "request": info.context,
            "token": token,
            "port": info.context.get_port(),
            "site_name": site.name,
            "domain": settings.SITE_URLS,
            "protocol": "https" if info.context.is_secure() else "http",
            "path": path,
            "timestamp": time.time(),
            **settings.AUTH.EMAIL_TEMPLATE_VARIABLES,
        }

    def send_activation_email(self, info, *args, **kwargs):
        email_context = self.get_email_context(
            info, settings.AUTH.ACTIVATION_PATH_ON_EMAIL, TokenAction.ACTIVATION
        )
        template = settings.AUTH.EMAIL_TEMPLATE_ACTIVATION
        subject = settings.AUTH.EMAIL_SUBJECT_ACTIVATION
        return self.send(subject, template, email_context, *args, **kwargs)

    # def resend_activation_email(self, info, *args, **kwargs):
    #     if self.verified is True:x
    #         raise UserAlreadyVerified
    #     email_context = self.get_email_context(
    #         info, settings.AUTH.ACTIVATION_PATH_ON_EMAIL, TokenAction.ACTIVATION
    #     )
    #     template = settings.AUTH.EMAIL_TEMPLATE_ACTIVATION_RESEND
    #     subject = settings.AUTH.EMAIL_SUBJECT_ACTIVATION_RESEND
    #     return self.send(subject, template, email_context, *args, **kwargs)

    # def send_password_set_email(self, info, *args, **kwargs):
    #     email_context = self.get_email_context(
    #         info, settings.AUTH.PASSWORD_SET_PATH_ON_EMAIL, TokenAction.PASSWORD_SET
    #     )
    #     template = settings.AUTH.EMAIL_TEMPLATE_PASSWORD_SET
    #     subject = settings.AUTH.EMAIL_SUBJECT_PASSWORD_SET
    #     return self.send(subject, template, email_context, *args, **kwargs)

    # def send_password_reset_email(self, info, *args, **kwargs):
    #     email_context = self.get_email_context(
    #         info, settings.AUTH.PASSWORD_RESET_PATH_ON_EMAIL, TokenAction.PASSWORD_RESET
    #     )
    #     template = settings.AUTH.EMAIL_TEMPLATE_PASSWORD_RESET
    #     subject = settings.AUTH.EMAIL_SUBJECT_PASSWORD_RESET
    #     return self.send(subject, template, email_context, *args, **kwargs)

    # def send_secondary_email_activation(self, info, email):
    #     if not self.email_is_free(email):
    #         raise EmailAlreadyInUse
    #     email_context = self.get_email_context(
    #         info,
    #         settings.AUTH.ACTIVATION_SECONDARY_EMAIL_PATH_ON_EMAIL,
    #         TokenAction.ACTIVATION_SECONDARY_EMAIL,
    #         secondary_email=email,
    #     )
    #     template = settings.AUTH.EMAIL_TEMPLATE_SECONDARY_EMAIL_ACTIVATION
    #     subject = settings.AUTH.EMAIL_SUBJECT_SECONDARY_EMAIL_ACTIVATION
    #     return self.send(subject, template, email_context, recipient_list=[email])

    # @classmethod
    # def email_is_free(cls, email):
    #     try:
    #         SEUser._default_manager.get(**{SEUser.EMAIL_FIELD: email})
    #         return False
    #     except Exception:
    #         pass
    #     try:
    #         UserStatus._default_manager.get(secondary_email=email)
    #         return False
    #     except Exception:
    #         pass
    #     return True

    # @classmethod
    # def clean_email(cls, email=False):
    #     if email:
    #         if cls.email_is_free(email) is False:
    #             raise EmailAlreadyInUse

    @classmethod
    def verify(cls, token):
        user = get_user_by_token(token)
        user_status = cls.objects.get(user=user)
        if user_status.verified is False:
            user_status.verified = True
            user_status.save(update_fields=["verified"])
            # user_verified.send(sender=cls, user=user)
            return user
        else:
            raise UserAlreadyVerified

    # @classmethod
    # def verify_secondary_email(cls, token):
    #     payload = get_token_payload(
    #         token,
    #         TokenAction.ACTIVATION_SECONDARY_EMAIL,
    #         settings.AUTH.EXPIRATION_SECONDARY_EMAIL_ACTIVATION_TOKEN,
    #     )
    #     secondary_email = payload.pop("secondary_email")
    #     if not cls.email_is_free(secondary_email):
    #         raise EmailAlreadyInUse
    #     user = SEUser._default_manager.get(**payload)
    #     user_status = cls.objects.get(user=user)
    #     user_status.secondary_email = secondary_email
    #     user_status.save(update_fields=["secondary_email"])

    # @classmethod
    # def unarchive(cls, user):
    #     user_status = cls.objects.get(user=user)
    #     if user_status.archived is True:
    #         user_status.archived = False
    #         user_status.save(update_fields=["archived"])

    # @classmethod
    # def archive(cls, user):
    #     user_status = cls.objects.get(user=user)
    #     if user_status.archived is False:
    #         user_status.archived = True
    #         user_status.save(update_fields=["archived"])

    # def swap_emails(self):
    #     if not self.secondary_email:
    #         raise WrongUsage
    #     with transaction.atomic():
    #         EMAIL_FIELD = SEUser.EMAIL_FIELD
    #         primary = getattr(self.user, EMAIL_FIELD)
    #         setattr(self.user, EMAIL_FIELD, self.secondary_email)
    #         self.secondary_email = primary
    #         self.user.save(update_fields=[EMAIL_FIELD])
    #         self.save(update_fields=["secondary_email"])

    # def remove_secondary_email(self):
    #     if not self.secondary_email:
    #         raise WrongUsage
    #     with transaction.atomic():
    #         self.secondary_email = None
    #         self.save(update_fields=["secondary_email"])
