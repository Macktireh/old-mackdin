from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='sign_in')
def Post_List_View(request, *args, **kwargs):
    template = 'post/post_list.html'
    return render(request, template)