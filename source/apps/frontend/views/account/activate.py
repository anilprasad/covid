from django.contrib.auth import login, get_user_model
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views import View

from source.apps.core.tokens.account.tokens import account_activation_token


class ActivateView(View):

    def get(self, request, uidb64, token):

        User = get_user_model()

        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user, backend='source.apps.user.backends.AuthBackend')
            messages.add_message(request, messages.SUCCESS, _('Your account has been successfully activated.'))
            return redirect('home')
        else:
            return render(request, 'account/activation_invalid.html')
