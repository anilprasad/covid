import uuid

from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from source.apps.core import media
from source.apps.core import fields
from source.apps.core.tasks.core.tasks import send_mail


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    User model
    """
    username = None
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    email = models.EmailField(_(u'Email address'), unique=True)
    first_name = models.CharField(_('First name'), max_length=150, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail.delay(subject=subject, message=message, to=self.email, **kwargs)

    class Meta:
        db_table = 'user'
        verbose_name = _(u'User')
        verbose_name_plural = _(u'Users')


class UserProfile(models.Model):
    """
    User profile model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, related_name='profile')
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    date_of_birth = models.DateField(blank=True, null=True, default='1985-03-25', verbose_name=_('Date of birth'))
    email_confirmed = models.BooleanField(default=False)
    phone = models.CharField(max_length=64, blank=True, null=True)
    picture = fields.ImageField(blank=True, null=True, upload_to=media.scramble_uploaded_filename, verbose_name=_('Profile picture'))

    @property
    def get_age(self):
        today = date.today()
        born = self.date_of_birth

        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    class Meta:
        db_table = 'user_profile'
        verbose_name = _(u'User profile')
        verbose_name_plural = _(u'Users profiles')


class UserPasswordRecoveryRequest(models.Model):
    """
    Keep track of password recovery requests
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    token = models.CharField(max_length=255, unique=True, blank=True)

    class Meta:
        db_table = 'user_password_recovery_request'
        verbose_name = _(u'User password recovery request')
        verbose_name_plural = _(u'Users password recovery requests')
