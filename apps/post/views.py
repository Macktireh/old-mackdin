from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from apps.post.models import Like, Post
from apps.post.forms import PostForm


@login_required(login_url='sign_in')
def post_create_list_view(request, *args, **kwargs):
    posts = Post.objects.all()
    user = request.user
    add_post = False
    
    if request.method == 'POST':
        AddPostForm = PostForm(request.POST or None, request.FILES or None)
        if AddPostForm.is_valid():
            instance = AddPostForm.save(commit=False)
            instance.author = user
            instance.save()
            print('#####################')
            print('Okkkkkkkkk')
            print('#####################')
            add_post = True
            
            return redirect('post_list')
    else:
        AddPostForm = PostForm()
        
    template = 'post/post_list.html'
    context = {
        'start_animation': 'feed',
        'posts': posts,
        'AddPostForm': AddPostForm,
        'add_post': add_post
    }
    return render(request, template, context)

def like_post(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like, created = Like.objects.get_or_create(user=user, post_id=post_id)
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
            # 'value': list(like.value),
            'likes': post_obj.liked.all().count()
        }
        return JsonResponse(data, safe=False)
    return redirect('post_list')

