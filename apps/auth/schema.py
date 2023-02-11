from .models import SecureUser
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from graphql_jwt import ObtainJSONWebToken
import graphql_social_auth

from django.contrib.auth import logout


from core.utils import convert_fields
from apps.auth.models import Company, LogAttempts, Profile, UserEmailLog
from apps.auth.mutations import (ArchiveAccount, DeleteAccount, Invite,
                                   PasswordChange, PasswordReset, PasswordSet,
                                   RefreshToken, Register,
                                   RemoveSecondaryEmail, ResendActivationEmail,
                                   RevokeToken, SendPasswordResetEmail,
                                   SendSecondaryEmailActivation, SlackAuthCode, SwapEmails,
                                   UpdateAccount, UpdateCompany, VerifyAccount,
                                   VerifySecondaryEmail, VerifyToken, VerfiyCname)
# from apps.auth.types import (CompanyNode, LogAttemptsNode, ProfileNode,
#                                UserEmailLogNode)
from apps.auth.types import (LogAttemptsNode,
                               UserEmailLogNode)

from .queries import CompanyQuery, MeQuery, UserQuery

class JSONWebTokenMixin:
    token = graphene.String()

    @classmethod
    def resolve(cls, root, info, social, **kwargs):
        try:
            from graphql_jwt.shortcuts import get_token
        except ImportError:
            raise ImportError(
                'django-graphql-jwt not installed.\n'
                'Use `pip install \'django-graphql-social-auth[jwt]\'`.')

        return cls(token=get_token(social.user))
    
class SocialAuthJWT(JSONWebTokenMixin, graphql_social_auth.relay.mutations.SocialAuthMutation):
    
    @classmethod
    def resolve(cls, root, info, social, **kwargs):
        logout(info.context)
        
        try:
            from graphql_jwt.shortcuts import get_token
        except ImportError:
            raise ImportError(
                'django-graphql-jwt not installed.\n'
                'Use `pip install \'django-graphql-social-auth[jwt]\'`.')

        if not Company.objects.filter(user_emp = social.user).exists():
            company_name = ''
            if social.provider == "google-oauth2" and not social.user.email.endswith('gmail.com'):
                company_name = social.user.email.split('@')[1].split('.')[0]
            else:
                company_name = social.user.email.split('@')[0]

            company, created = Company.objects.get_or_create(owner = social.user, name=company_name.replace('.', '').replace('_', ''))
            company.user_emp.add(social.user)
            company.save()
            social.user.save()
            Profile.objects.get_or_create(user = social.user, company=company)
        
        return cls(token=get_token(social.user))


class VerifiedObtainJSONWebToken(ObtainJSONWebToken):
    @classmethod
    def mutate(cls, root, info, **kwargs):
        user = SecureUser.objects.get(email = kwargs.get('email'))
        if user.status.verified:
            return super().mutate(root, info, **kwargs)
        raise Exception('You need to verify you account first.')

class Mutation:
    register = Register.Field()
    invite = Invite.Field()
    verify_account = VerifyAccount.Field()
    resend_activation_email = ResendActivationEmail.Field()
    send_password_reset_email = SendPasswordResetEmail.Field()
    password_reset = PasswordReset.Field()
    password_set = PasswordSet.Field()  # For passwordless registration
    password_change = PasswordChange.Field()
    update_account = UpdateAccount.Field()
    archive_account = ArchiveAccount.Field()
    delete_account = DeleteAccount.Field()
    send_secondary_email_activation = SendSecondaryEmailActivation.Field()
    verify_secondary_email = VerifySecondaryEmail.Field()
    swap_emails = SwapEmails.Field()
    remove_secondary_email = RemoveSecondaryEmail.Field()
    update_company = UpdateCompany.Field()

    # django-graphql-jwt inheritances
    token_auth = VerifiedObtainJSONWebToken.Field()
    verify_token = VerifyToken.Field()
    refresh_token = RefreshToken.Field()
    revoke_token = RevokeToken.Field()
    
    social_auth = SocialAuthJWT.Field()
    slack_auth_code = SlackAuthCode.Field()

    verify_cname = VerfiyCname.Field()


class Query(UserQuery, MeQuery, CompanyQuery):
    companies = DjangoFilterConnectionField(CompanyNode)
    company_by_parameters = graphene.Field(
        CompanyNode,
        **convert_fields(Company, only_fields=["id"]),
    )

    profiles = DjangoFilterConnectionField(ProfileNode)
    profile_by_parameters = graphene.Field(
        ProfileNode,
        **convert_fields(Profile, only_fields=["id"]),
    )

    log_attempts = DjangoFilterConnectionField(LogAttemptsNode)
    log_attempts_by_parameters = graphene.Field(
        LogAttemptsNode,
        **convert_fields(LogAttempts, only_fields=["id"]),
    )

    user_email_logs = DjangoFilterConnectionField(UserEmailLogNode)

    user_email_logs_by_parameters = graphene.Field(
        UserEmailLogNode,
        **convert_fields(UserEmailLog, only_fields=["id"]),
    )

    def resolve_company_by_parameters(self, info, **kwargs):
        return CompanyNode.get_node_by_parameters(info, **kwargs)

    def resolve_profile_by_parameters(self, info, **kwargs):
        return ProfileNode.get_node_by_parameters(info, **kwargs)

    def resolve_log_attempts_by_parameters(self, info, **kwargs):
        return LogAttemptsNode.get_node_by_parameters(info, **kwargs)

    def resolve_user_email_logs_by_parameters(self, info, **kwargs):
        return UserEmailLogNode.get_node_by_parameters(info, **kwargs)
