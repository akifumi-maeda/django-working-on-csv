from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    '''ログインフォーム'''

    def __init__(self, request, *args, **kwargs):
        super().__init__(request=request, *args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label