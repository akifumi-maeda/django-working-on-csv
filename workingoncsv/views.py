from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

class MyLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

class MyLogoutView(LogoutView):
    template_name = 'registration/logout.html'