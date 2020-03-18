from django.contrib.auth.views import LoginView
from source.apps.core.forms.account.forms import LoginForm


class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'
    redirect_authenticated_user = True
