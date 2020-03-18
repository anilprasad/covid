from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from source.apps.core.forms.account.forms import PasswordResetForm


class PasswordResetView(PasswordResetView):
    email_template_name = 'email/account/password_reset.html'
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = _('Password reset')
    success_url = reverse_lazy('password_reset_done')
    template_name = 'account/password_reset.html'
    title = _('Password reset')
