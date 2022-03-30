from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()
from apps.friends.models import Relationship
from apps.profiles.models import Profile


@login_required(login_url='sign_in')
def invites_received_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    qs = Relationship.objects.invatation_received(profile)
    
    template = 'friends/invites.html'
    context = {
        'qs': qs,
    }
    
    return render(request, template, context)


@login_required(login_url='sign_in')
def list_profiles_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_exclude_me(user)
    
    template = 'friends/mynetwork.html'
    context = {
        'qs': qs,
    }
    
    return render(request, template, context)


@login_required(login_url='sign_in')
def invites_list_profiles_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invites(user)
    
    template = 'friends/invites_list_profiles.html'
    context = {
        'qs': qs,
    }
    
    return render(request, template, context)
