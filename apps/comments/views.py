import json
from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from apps.post.models import Post
from apps.comments.models import Comment, ReponseComment, LikeComment
from apps.comments.forms import CommentForm, ReponseCommentForm

User = get_user_model()

@csrf_exempt
def add_comment(request, post_id):
    user = request.user
    if request.method == 'POST':
        # post_id = request.POST.get('post_id')
        message = request.POST.get('message')
        
        print(post_id)
        print(message)
        
        comment_post = Comment(author=user, post_id=post_id, message=message)
        comment_post.save()
        
        qs_comment = Comment.objects.select_related("author").select_related("post").get(id=comment_post.id)
        qs_user = User.objects.prefetch_related("profile")
        
        
        # for obj in qs_comment:
        item = {
            'id': qs_comment.id,
            'comment_author': qs_comment.author.email,
            # 'comment_author_id': qs_comment.author.id,
            'comment_author_first_name': qs_comment.author.first_name,
            'comment_author_last_name': qs_comment.author.last_name,
            'comment_message': qs_comment.message,
            'comment_date_added': qs_comment.date_added.strftime("%d-%m-%Y %H:%M:%S"),
            
            # 'post_id': qs_comment.post.id,
            'post_author': qs_comment.post.author.email,
            # 'post_message': qs_comment.post.message,
            # 'post_img': qs_comment.post.img.url,
            'user_profile_bio': qs_user.get(id=qs_comment.author.id).profile.bio,
            'user_profile_img': qs_user.get(id=qs_comment.author.id).profile.img_profile.url,
            'current_user': request.user.email,
        }
            # data.append(item)
        data = [item]
        return JsonResponse({'data': data})
    return redirect('post_list')
        
    
    # return JsonResponse({'data': data})



def comment_all_data(request):  
    qs_comment = Comment.objects.select_related("author").select_related("post").all()
    qs_user = User.objects.prefetch_related("profile")
    
    data = []
    
    for obj in qs_comment:
        item = {
            'id': obj.id,
            'comment_author': obj.author.email,
            'comment_author_id': obj.author.id,
            'comment_message': obj.message,
            'comment_date_added': obj.date_added.strftime("%d-%m-%Y %H:%M:%S"),
            'post_id': obj.post.id,
            'post_author': obj.post.author.email,
            'post_message': obj.post.message,
            'post_img': obj.post.img.url,
            'user_img_bio': qs_user.get(id=obj.author.id).profile.bio,
            'user_img_profile': qs_user.get(id=obj.author.id).profile.img_profile.url,
            'current_user': request.user.email,
        }
        data.append(item)
  
    return JsonResponse({'data': data})