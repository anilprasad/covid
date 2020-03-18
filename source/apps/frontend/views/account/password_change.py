from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from source.apps.core.forms.account.forms import PasswordChangeForm


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_change_done')
    template_name = 'account/password_change.html'
    title = _('Password change')
