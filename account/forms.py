from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Valid Email Address Needed')

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")

