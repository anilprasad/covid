from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save

from rest_framework.authtoken.models import Token

from source.apps.core.models.user.models import UserProfile


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.profile.save()


def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save_signal_receiver_master(*args, **kwargs):
    create_user_profile(*args, **kwargs)
    create_auth_token(*args, **kwargs)
