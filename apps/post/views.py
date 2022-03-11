from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from apps.post.models import Post


@login_required(login_url='sign_in')
def Post_List_View(request, *args, **kwargs):
    posts = Post.objects.all()
    template = 'post/post_list.html'
    context = {
        'start_animation': 'feed',
        'posts': posts
    }
    return render(request, template, context)