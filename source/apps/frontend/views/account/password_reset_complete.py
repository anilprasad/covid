from django.contrib.auth.views import PasswordResetCompleteView
from django.utils.translation import gettext_lazy as _


class PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'
    title = _('Password reset complete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
