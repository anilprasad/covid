from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.forms.models import model_to_dict

from source.apps.core.forms.account.forms import AccountForm


class AccountView(View):

    def get(self, request):
        form = AccountForm(initial=model_to_dict(request.user))

        context = {
            'form': form
        }

        return render(request, 'account/account.html', context)

    def post(self, request):
        form = AccountForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, _('Your account has been successfully saved.'))
            return redirect('account')

        return render(request, 'account/account.html', {
            'form': form
        })
