from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from django import forms
from django.contrib.auth import authenticate

from .models import User

User = get_user_model()


# admin forms
class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        error_messages = {
            "username": {"unique": _("This username has already been taken.")}
        }

# user forms

class RegistrationForm(admin_forms.UserCreationForm):

    email = forms.EmailField(max_length=255, help_text="Required. Add valid email address.")

    class Meta:
        model = User
        fields = ('email',)