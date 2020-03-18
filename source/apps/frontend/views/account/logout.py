from django.contrib.auth.views import LogoutView


class LogoutView(LogoutView):
    template_name = 'home/index.html'
