from django.urls import re_path

from source.apps.frontend.views.account.account import AccountView
from source.apps.frontend.views.account.signup import SignupView
from source.apps.frontend.views.account.login import LoginView
from source.apps.frontend.views.account.logout import LogoutView
from source.apps.frontend.views.account.password_reset import PasswordResetView
from source.apps.frontend.views.account.password_reset_done import PasswordResetDoneView
from source.apps.frontend.views.account.password_reset_confirm import PasswordResetConfirmView
from source.apps.frontend.views.account.password_reset_complete import PasswordResetCompleteView
from source.apps.frontend.views.account.password_change import PasswordChangeView
from source.apps.frontend.views.account.password_change_done import PasswordChangeDoneView
from source.apps.frontend.views.account.activate import ActivateView


urlpatterns = [
    re_path(r'^$', AccountView.as_view(), name='account'),
    re_path(r'^signup/$', SignupView.as_view(), name='signup'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^password-reset/$', PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^password-reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(r'^password-reset/reset/done/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    re_path(r'^password-change/$', PasswordChangeView.as_view(), name='password_change'),
    re_path(r'^password-change/done/$', PasswordChangeDoneView.as_view(), name='password_change_done'),
    # re_path(r'^activation-sent/$', core_views.account_activation_sent, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            ActivateView.as_view(), name='account_activate'),
]
