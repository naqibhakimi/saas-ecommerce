from django.conf import settings as django_settings
from django.db.models.signals import post_save
from django.dispatch import Signal, receiver


@receiver(post_save, sender=django_settings.AUTH_USER_MODEL)
def create_user_status(sender, instance, created, **kwargs):
    if created:
        from .models import Profile, UserStatus

        UserStatus._default_manager.get_or_create(user=instance)
        # Profile._default_manager.get_or_create(user=instance)


user_registered = Signal()
user_verified = Signal()


# def delete_company(sender, instance, **kwargs):
#     company_id = instance.id
#     try:
#         com = Company.objects.get(id=company_id)
#         try:
#             for u in com.user_emp.all():
#                 if u != com.owner:
#                     u.delete()

#         except Exception as e:
#             print('error while Deleting the company users', str(e))

#     except Exception as e:
#         print("error in getting the company object", str(e))


# pre_delete.connect(delete_company, sender=Company)


# @receiver(post_save, sender=encUsers)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         userProfile = Profile.objects.create(user=instance)
#     # else:
#     #     instance.profile.save()


# @receiver(post_save, sender=SocialAccount)
# def edit_user_profile(sender, instance, created, **kwargs):
#     if created:
#         try:
#             print("social account created")
#             userProfile = Profile.objects.filter(user=instance.user)
#             if userProfile.exists():
#                 userProfile = userProfile.first()

#                 if userProfile.name is None:
#                     userProfile.name = instance.extra_data['name']
#                 try:
#                     if userProfile.company is None:

#                         company = Company.objects.create(
#                             owner=userProfile.user)
#                         company.user_emp.add(userProfile.user)
#                         company.save()
#                         userProfile.company = company
#                         userProfile.role = "admin"
#                         userProfile.active = True
#                 except Exception as e:
#                     print("exception sa", e)
#                 userProfile.save()
#         except Exception as e:
#             print("Social Account Exception ", e)
