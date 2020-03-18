from django.contrib.auth.views import PasswordResetDoneView
from django.utils.translation import gettext_lazy as _


class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'
    title = _('Please check your email for instructions.')
