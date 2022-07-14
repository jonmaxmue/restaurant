from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class AuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Telefonnummer',
        widget=forms.TextInput(attrs={'autofocus': True})
    )