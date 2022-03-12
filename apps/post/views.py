from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from apps.post.models import Like, Post


@login_required(login_url='sign_in')
def Post_List_View(request, *args, **kwargs):
    posts = Post.objects.all()
    template = 'post/post_list.html'
    context = {
        'start_animation': 'feed',
        'posts': posts
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