import cloudinary
import os
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from apps.comments.views import comment_view
from apps.post.models import LikePost, Post
from apps.post.forms import PostForm
from apps.comments.models import Comment, ReponseComment, LikeComment
from apps.comments.forms import CommentForm, ReponseCommentForm



@login_required(login_url='sign_in')
def post_create_list_view(request, *args, **kwargs):
    posts = Post.objects.all()
    user = request.user
    post_form = False
    
    AddPostForm = PostForm()
    
    if "submit_p_form" in request.POST:
        AddPostForm = PostForm(request.POST, request.FILES)
        if AddPostForm.is_valid():
            instance = AddPostForm.save(commit=False)
            instance.author = user
            instance.save()
            AddPostForm = PostForm()
            
            return redirect('post:post_list')
    
    template = 'post/post_list.html'
    context = {
        'start_animation': 'feed',
        'posts': posts,
        'AddPostForm': AddPostForm,
        'post_form': post_form,
    }
    context.update(comment_view(request))
    return render(request, template, context)


@login_required(login_url='sign_in')
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_form = False
    post_detail = True
    
    template = 'post/post_list.html'
    context = {
        'start_animation': 'feed',
        'post': post,
        'post_form': post_form,
        'post_detail': post_detail,
    }
    context.update(comment_view(request))
    return render(request, template, context)


@login_required(login_url='sign_in')
def update_post(request, post_id):
    post_edit = get_object_or_404(Post, id=post_id)
    posts = Post.objects.all()
    post_form = True
    
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if post_edit.img:
                if len(post_edit.img) > 0:
                    cloudinary.uploader.destroy(post_edit.img.public_id)
                    # os.remove(post_edit.img.path)
            post_edit.img = request.FILES['img']      
        post_edit.message = request.POST.get('message')
        post_edit.save()
        return redirect('post:post_list')

        
    template = 'post/post_list.html'
    context = {
        'start_animation': 'feed',
        'posts': posts,
        'post_edit': post_edit,
        'post_form': post_form
    }
    return render(request, template, context)


# def add_post(request):
#     user = request.user
#     AddPostForm = PostForm(request.POST or None, request.FILES or None)
#     if request.is_ajax():
#         if AddPostForm.is_valid():
#             instance = AddPostForm.save(commit=False)
#             instance.author = user
#             instance.save()
#             post = Post.objects.values()
#             return JsonResponse({'status': 'success', 'post_data': list(post)})
#         else:
#             return JsonResponse({'status': 'error'})
   

@login_required(login_url='sign_in')
def delete_post(request, post_id):
    user = request.user
    # if request.method == 'POST':
    #     p_id = request.POST.get('post_id')
    #     instance = Post.objects.get(pk=p_id)
    #     if user == instance.author:
    #         instance.delete()
    #         return JsonResponse({'status': 'Post supprimer'})
    # else:
    #     return JsonResponse({'status': 'error'})
    instance = get_object_or_404(Post, id=post_id)
    if user == instance.author:
        instance.delete()
    return redirect('post:post_list')
        
        
@login_required(login_url='sign_in')
def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = LikePost.objects.get_or_create(user=user, post_id=post_id)
        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
                like.value='Like'
        else:
            like.value='Like'

        post_obj.save()
        like.save()
        
        data = {
            'value': str(like.value),
            'likes': post_obj.liked.all().count()
        }
        return JsonResponse(data, safe=False)
    return redirect('post:post_list')
