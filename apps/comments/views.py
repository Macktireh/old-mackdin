from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from apps.comments.models import Comment, ReponseComment, LikeComment
from apps.comments.forms import CommentForm, ReponseCommentForm