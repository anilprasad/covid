from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext_lazy as _
from django.views import View

from source.apps.core.forms.account.forms import SignupForm
from source.apps.core.tokens.account.tokens import account_activation_token


class SignupView(View):
    form = SignupForm
    template_name = 'account/signup.html'

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect('home')

        return render(request, self.template_name, {
            'form': self.form
        })

    def post(self, request, *args, **kwargs):

        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = _('Activate your %(app_name)s account') % {'app_name': settings.APP_NAME}
            message = render_to_string('email/account/account_activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)

            messages.add_message(
                request,
                messages.INFO,
                _('Your account has been created. Check your email (including spam/junk folder) for an activation link.')
            )

            return redirect('home')

        return render(request, self.template_name, {'form': form})
