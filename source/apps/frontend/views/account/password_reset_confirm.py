from django.contrib.auth.views import PasswordResetConfirmView
from source.apps.core.forms.account.forms import SetPasswordForm


class PasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    template_name = 'account/password_reset_confirm.html'
