from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from catalog.forms import StyleFormMixin
from users.models import CustomUser


class UserRegisterForm(StyleFormMixin, UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ['email', 'password1', 'password2']


class UserLoginForm(StyleFormMixin, AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']