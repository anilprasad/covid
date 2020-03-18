from django.contrib.auth.views import PasswordChangeDoneView
from django.utils.translation import gettext_lazy as _


class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'account/password_change_done.html'
    title = _('Password change successful')
