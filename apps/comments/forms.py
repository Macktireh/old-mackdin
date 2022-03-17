from django.forms import forms
from django.utils.translation import gettext_lazy as _

from apps.comments.models import Comment, ReponseComment


class CommentForm(forms.ModelForm):
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'cols':'65', 'rows':'1', 'id':'message_comment_id', 'placeholder':'Ajouter un commentaire...'}))
    model = Comment
    fields = ('message',)
    

class ReponseCommentForm(forms.ModelForm):
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'cols':'65', 'rows':'1', 'id':'message_comment_id', 'placeholder':'Ajouter une réponse...'}))
    model = ReponseComment
    fields = ('message',)