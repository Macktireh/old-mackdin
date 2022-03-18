from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from apps.comments.models import Comment, ReponseComment, LikeComment
from apps.comments.forms import CommentForm, ReponseCommentForm


# def CommentView(request):
#     form_comment = CommentForm(request.POST)
#     form_reponse = ReponseCommentForm(request.POST)
#     context = {
#         'form_comment': form_comment,
#         'form_reponse': form_reponse
#     }
#     return render(request, 'comments/index.html', context)