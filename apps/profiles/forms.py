from dataclasses import fields
from tkinter import Widget
from django import forms
from django.utils.translation import gettext_lazy as _
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.contrib.auth import get_user_model

from apps.profiles.models import Profile

User = get_user_model()

class ProfileForm(forms.ModelForm):
    # bio = forms.CharField(required=False, widget=forms.Textarea(
    #     attrs={'cols':'65', 'rows':'2', 'id':'textarea_id', 'placeholder':'Ajouter un post'}))
    # description = forms.CharField(required=False, widget=forms.Textarea(
    #     attrs={'cols':'65', 'rows':'8', 'id':'textarea_id', 'placeholder':'Ajouter un post'}))
    class Meta:
        model = Profile
        exclude = ('user', 'number_views',)
        widgets = {
            'bio': forms.Textarea(attrs={'cols':'80', 'rows':'3', 'id':'textarea_id', 'placeholder':'Ajouter un post'}),
            'description': forms.Textarea(attrs={'cols':'80', 'rows':'8', 'id':'textarea_id', 'placeholder':'Ajouter un post'})
        }
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)