from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import BaseUserCreationForm

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Repeat Password")

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)



