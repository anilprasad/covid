from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import (
    AuthenticationForm, UsernameField, UserCreationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
)
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _

from source.apps.core.email import send_email
from source.apps.core.models.user.models import User


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control form-control-lg',
                'placeholder': _('Email'),
            }
        )
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': _('Password')
            }
        ),
    )


class SignupForm(UserCreationForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    username = forms.CharField(
        max_length=32,
        help_text=_('Please type a valid username.'),
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control form-control-lg',
                'placeholder': _('Username'),
            }
        ),
    )

    email = forms.EmailField(
        max_length=254,
        help_text=_('Please type a valid email address.'),
        widget=forms.EmailInput(
            attrs={
                'autofocus': True,
                'class': 'form-control form-control-lg',
                'placeholder': _('Email'),
            }
        ),
    )

    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': _('Password')
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )

    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': _('Confirm password')
            }
        ),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', )


class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'placeholder': _('Email'),
            }
        ),
    )

    def send_mail(self, subject_template_name, email_template_name,
                  context, from_email, to_email, html_email_template_name=None):

        send_email(
            template=email_template_name,
            subject=subject_template_name,
            to=to_email,
            data=context
        )


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'autofocus': True,
                'class': 'form-control form-control-lg',
                'placeholder': _('Current password')

            }
        ),
    )

    new_password1 = forms.CharField(
        label=_("New password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': _('New password')
            }
        ),
        # help_text=password_validation.password_validators_help_text_html(),
    )

    new_password2 = forms.CharField(
        label=_("Confirm new password"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': _('Confirm new password')
            }
        ),
        strip=False,
        # help_text=_("Enter the same password as before, for verification."),
    )


class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': _('Password')
            }
        ),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': _('Confirm password')
            }
        ),
    )


class AccountForm(ModelForm):
    first_name = forms.CharField(
        label=_("First name"),
        strip=True,
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control form-control-lg',
                'placeholder': _('First name')

            }
        ),
    )

    last_name = forms.CharField(
        label=_('Last name'),
        strip=True,
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control form-control-lg',
                'placeholder': _('Last name')

            }
        ),
    )

    email = forms.EmailField(
        max_length=254,
        help_text=_('Please type a valid email address.'),
        widget=forms.EmailInput(
            attrs={
                'autofocus': True,
                'class': 'form-control form-control-lg',
                'placeholder': _('Email'),
            }
        ),
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )
