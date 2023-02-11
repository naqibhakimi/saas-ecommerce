from django.db import models
from apps.core.models import BaseModel
from django.contrib.auth.models import AbstractUser
import time
from apps.core.interval_async_timer import RepeatingAsyncTimer
from apps.core.saas_domain_manager import SaasDomainManager
import dns.resolver
from django.conf import settings as django_settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.mail import send_mail
from django.db import models, transaction
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from PIL import Image

from apps.core.decorators.decorators import add_info

from .constants import TokenAction
from .exceptions import EmailAlreadyInUse, UserAlreadyVerified, WrongUsage
from .settings import graphql_auth_settings as app_settings
from .signals import user_verified
from .utils import get_token, get_token_payload

from apps.core.middlewares import thread_local
from apps.customer.models import Address


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


# class User(AbstractUser, BaseModel):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=256, blank=True)
#     last_name = models.CharField(max_length=256, blank=True)
#     # addresses = models.ManyToManyField(
#     #     Address, blank=True, related_name="+"
#     # )
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     note = models.TextField(null=True, blank=True)
#     default_shipping_address = models.ForeignKey(
#         Address, related_name="+", null=True, blank=True, on_delete=models.SET_NULL
#     )
#     # default_billing_address = models.ForeignKey(
#     #     Address, related_name="+", null=True, blank=True, on_delete=models.SET_NULL
#     # )
#     # avatar = models.ImageField(upload_to="user-avatars", blank=True, null=True)
#     # jwt_token_key = models.CharField(
#     #     max_length=12, default=partial(get_random_string, length=12)
#     # )
#     # language_code = models.CharField(
#     #     max_length=35, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE
#     # )
#     # search_document = models.TextField(blank=True, default="")
#     # uuid = models.UUIDField(default=uuid4, unique=True)

#     USERNAME_FIELD = "email"

#     # objects = UserManager()


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


# class SEUser(AbstractBaseUser, PermissionsMixin):
class SEUser(AbstractBaseUser):
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
        full_name = "%s %s" % (self.first_name, self.last_name)
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
        return "%s - status" % (self.user)

    def send(self, subject, template, context, recipient_list=None):
        _subject = render_to_string(
            subject, context).replace("\n", " ").strip()
        html_message = render_to_string(template, context)
        message = strip_tags(html_message)

        return send_mail(
            subject=_subject,
            from_email=app_settings.EMAIL_FROM,
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
        # TODO(naqib): fix port on production server

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
            **app_settings.EMAIL_TEMPLATE_VARIABLES,
        }

    def send_activation_email(self, info, *args, **kwargs):
        email_context = self.get_email_context(
            info, app_settings.ACTIVATION_PATH_ON_EMAIL, TokenAction.ACTIVATION
        )
        template = app_settings.EMAIL_TEMPLATE_ACTIVATION
        subject = app_settings.EMAIL_SUBJECT_ACTIVATION
        return self.send(subject, template, email_context, *args, **kwargs)

    def resend_activation_email(self, info, *args, **kwargs):
        if self.verified is True:
            raise UserAlreadyVerified
        email_context = self.get_email_context(
            info, app_settings.ACTIVATION_PATH_ON_EMAIL, TokenAction.ACTIVATION
        )
        template = app_settings.EMAIL_TEMPLATE_ACTIVATION_RESEND
        subject = app_settings.EMAIL_SUBJECT_ACTIVATION_RESEND
        return self.send(subject, template, email_context, *args, **kwargs)

    def send_password_set_email(self, info, *args, **kwargs):
        email_context = self.get_email_context(
            info, app_settings.PASSWORD_SET_PATH_ON_EMAIL, TokenAction.PASSWORD_SET
        )
        template = app_settings.EMAIL_TEMPLATE_PASSWORD_SET
        subject = app_settings.EMAIL_SUBJECT_PASSWORD_SET
        return self.send(subject, template, email_context, *args, **kwargs)

    def send_password_reset_email(self, info, *args, **kwargs):
        email_context = self.get_email_context(
            info, app_settings.PASSWORD_RESET_PATH_ON_EMAIL, TokenAction.PASSWORD_RESET
        )
        template = app_settings.EMAIL_TEMPLATE_PASSWORD_RESET
        subject = app_settings.EMAIL_SUBJECT_PASSWORD_RESET
        return self.send(subject, template, email_context, *args, **kwargs)

    def send_secondary_email_activation(self, info, email):
        if not self.email_is_free(email):
            raise EmailAlreadyInUse
        email_context = self.get_email_context(
            info,
            app_settings.ACTIVATION_SECONDARY_EMAIL_PATH_ON_EMAIL,
            TokenAction.ACTIVATION_SECONDARY_EMAIL,
            secondary_email=email,
        )
        template = app_settings.EMAIL_TEMPLATE_SECONDARY_EMAIL_ACTIVATION
        subject = app_settings.EMAIL_SUBJECT_SECONDARY_EMAIL_ACTIVATION
        return self.send(subject, template, email_context, recipient_list=[email])

    @classmethod
    def email_is_free(cls, email):
        try:
            SEUser._default_manager.get(**{SEUser.EMAIL_FIELD: email})
            return False
        except Exception:
            pass
        try:
            UserStatus._default_manager.get(secondary_email=email)
            return False
        except Exception:
            pass
        return True

    @classmethod
    def clean_email(cls, email=False):
        if email:
            if cls.email_is_free(email) is False:
                raise EmailAlreadyInUse

    @classmethod
    def verify(cls, token):
        payload = get_token_payload(
            token, TokenAction.ACTIVATION, app_settings.EXPIRATION_ACTIVATION_TOKEN
        )
        user = SEUser._default_manager.get(**payload)
        user_status = cls.objects.get(user=user)
        if user_status.verified is False:
            user_status.verified = True
            user_status.save(update_fields=["verified"])
            user_verified.send(sender=cls, user=user)
            return user
        else:
            raise UserAlreadyVerified

    @classmethod
    def verify_secondary_email(cls, token):
        payload = get_token_payload(
            token,
            TokenAction.ACTIVATION_SECONDARY_EMAIL,
            app_settings.EXPIRATION_SECONDARY_EMAIL_ACTIVATION_TOKEN,
        )
        secondary_email = payload.pop("secondary_email")
        if not cls.email_is_free(secondary_email):
            raise EmailAlreadyInUse
        user = SEUser._default_manager.get(**payload)
        user_status = cls.objects.get(user=user)
        user_status.secondary_email = secondary_email
        user_status.save(update_fields=["secondary_email"])

    @classmethod
    def unarchive(cls, user):
        user_status = cls.objects.get(user=user)
        if user_status.archived is True:
            user_status.archived = False
            user_status.save(update_fields=["archived"])

    @classmethod
    def archive(cls, user):
        user_status = cls.objects.get(user=user)
        if user_status.archived is False:
            user_status.archived = True
            user_status.save(update_fields=["archived"])

    def swap_emails(self):
        if not self.secondary_email:
            raise WrongUsage
        with transaction.atomic():
            EMAIL_FIELD = SEUser.EMAIL_FIELD
            primary = getattr(self.user, EMAIL_FIELD)
            setattr(self.user, EMAIL_FIELD, self.secondary_email)
            self.secondary_email = primary
            self.user.save(update_fields=[EMAIL_FIELD])
            self.save(update_fields=["secondary_email"])

    def remove_secondary_email(self):
        if not self.secondary_email:
            raise WrongUsage
        with transaction.atomic():
            self.secondary_email = None
            self.save(update_fields=["secondary_email"])

    class Meta:
        app_label = "secure_auth"


def check_domain(*args, **kwargs):
    # from subscription.models import Subscription
    # company = kwargs.get('company')
    # brand_domain = kwargs.get('domain')
    
    # domain_manager = SaasDomainManager(
    #     settings.CLOUD_FLARE_ZONEID, settings.CLOUD_FLARE_KEY)

    # if company.brand_domain != brand_domain:
    #      domain_manager.delete(brand_domain)
    # if Subscription.objects.filter(company_membership=company.companymembership, trial=False, company_membership__membership__level__gt=1).exists():
    #     company.cname = domain_manager.check_cname(company.brand_domain)
    #     company.save()
    #     domain_manager.create(company.brand_domain)
    pass


# class Company(models.Model):
#     owner = models.OneToOneField(
#         SEUser, on_delete=models.CASCADE, blank=True, null=True, related_name="owner"
#     )
#     name = models.CharField(
#         max_length=100,
#         error_messages={
#             "unique": "This company has already been registered.",
#             "required": "Company name must not be empty.",
#             "blank": "Company name must not be empty.",
#             "null": "Company name must not be empty.",
#         },
#     )

#     header_text = models.CharField(
#         max_length=100, blank=True, null=True, default="Company header")

#     user_emp = models.ManyToManyField(
#         SEUser, blank=True, related_name="employee")
#     company_logo = models.ImageField(null=True, blank=True)
#     company_header_color = models.CharField(
#         max_length=10, blank=True, null=True, default="#FFFFFF"
#     )
#     company_text_color = models.CharField(
#         max_length=10, blank=True, null=True, default="#000000"
#     )
#     active = models.BooleanField(default=True)

#     domain = models.CharField(
#         max_length=100, blank=True, null=True, unique=True)
#     cname = models.CharField(max_length=100, blank=True, null=True, default="")
#     brand_domain = models.CharField(
#         max_length=100, blank=True, null=True, unique=True)

#     # TODO(naqib): remove port number when we are using production
#     @property
#     def company_logo_url(self):
#         if self.company_logo:
#             return f'{self.company_logo.url}'
#         else:
#             return ''

#     class Meta:
#         verbose_name = "Company"
#         verbose_name_plural = "Companies"

#     def __str__(self):
#         return f'{self.name}: {self.brand_domain}: {self.domain}'

#     def clean_name(self):
#         return self.name.replace(' ', '').lower()

#     def save(self, *args, **kwargs):
#         print('saveing model ----------------------------')
#         import random
#         if not self.pk:
#             self.domain = f'{self.clean_name()}'
#             if Company.objects.filter(domain=self.domain).exists():
#                 self.domain = f'{self.clean_name()}{random.randint(1000, 9999)}'
#                 self.brand_domain = f'secure.{self.domain}.com'
#             else:
#                 self.brand_domain = f'secure.{self.domain}.com'

#         if self.companymembership.membership.level < 2:
#             self.brand_domain = f'secure.{self.domain}.com'

#         if self.company_logo:
#             try:
#                 self.company_logo = self.compressImage(self.company_logo)
#             except:
#                 pass
#         super(Company, self).save(*args, **kwargs)

#     def compressImage(self, uploadedImage):
#         imageTemproary = Image.open(uploadedImage)
#         outputIoStream = BytesIO()
#         imageTemproaryResized = imageTemproary.thumbnail((100, 100))
#         imageTemproary.save(outputIoStream, format="PNG", quality=60)
#         outputIoStream.seek(0)
#         uploadedImage = InMemoryUploadedFile(
#             outputIoStream,
#             "ImageField",
#             "%s.png" % uploadedImage.name.split(".")[0],
#             "image/png",
#             sys.getsizeof(outputIoStream),
#             None,
#         )
#         return uploadedImage


# class Profile(models.Model):
#     EmpRole = (
#         ("admin", "Admin"),
#         ("user", "User"),
#     )
#     user = models.OneToOneField(SEUser, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100, blank=True, null=True)
#     company = models.ForeignKey(
#         Company, on_delete=models.SET_NULL, blank=True, null=True
#     )
#     role = models.CharField(
#         max_length=20, choices=EmpRole, blank=True, null=True)
#     active = models.BooleanField(default=False)

#     date_joined = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = "Profile"
#         verbose_name_plural = "Profiles"

#     def __str__(self):
#         return self.user.email


class LogAttempts(BaseModel):
    email = models.EmailField(unique=True)
    login_attempts = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    duration_before_next_attempt = models.DateTimeField(blank=True, null=True)

    locked_out = models.BooleanField(default=False)


# class UserEmailLog(BaseModel):
#     email = models.EmailField(unique=True)
#     trial = models.BooleanField(default=False)
#     trial_end_date = models.DateTimeField(null=True)
#     user_account_delete_attempts = models.IntegerField(default=0)
