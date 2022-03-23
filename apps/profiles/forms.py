from tkinter import Widget
from django import forms
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from apps.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    # phone = PhoneNumberField(widget=PhoneNumberPrefixWidget())
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('Phone')}),required=False)
    class Meta:
        model = Profile
        exclude = ('user',)