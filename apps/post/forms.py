from django import forms
from django.forms import fields
from apps.post.models import Like, Post
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    """Form definition for Post."""
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'cols':'65', 'rows':'2', 'id':'textarea_id', 'placeholder':'Ajouter un post'}))
    img = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'id':'file', 'class':'form-input-file'}))
    class Meta:
        """Meta definition for Postform."""
        model = Post
        fields = ('message', 'img',)
