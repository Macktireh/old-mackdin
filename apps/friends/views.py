from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db.models import Q

User = get_user_model()
from apps.friends.models import Relationship
from apps.profiles.models import Profile


def list_relation_receiver_and_sender(request):
    qs = Profile.objects.get_all_profiles_to_invites(request.user)
    user = User.objects.get(email__iexact=request.user.email)
    profile = Profile.objects.get(user=user)
    
    qs_relation_receiver = Relationship.objects.filter(sender=profile)
    qs_relation_sender = Relationship.objects.filter(receiver=profile)
    
    list_relation_receiver = []
    for item in qs_relation_receiver:
        list_relation_receiver.append(item.receiver.user)
    
    list_relation_sender = []
    for item in qs_relation_sender:
        list_relation_sender.append(item.sender.user)
    
    is_empty = False
    if len(qs) == 0:
        is_empty = True
        
    template = 'friends/mynetwork.html'        
    context = {
        'qs': qs,
        'list_relation_receiver': list_relation_receiver,
        'list_relation_sender': list_relation_sender,
        'is_empty': is_empty,
    }
        
    return template, context


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
def my_friends_invites_profiles_view(request):
    qs = Profile.objects.get_all_profiles_exclude_me(request.user)
    
    template = 'friends/mynetwork.html'
    context = {
        'qs': qs,
        'page': 'my_friends',
        'start_animation': 'my_network'
    }
    
    return render(request, template, context)


@login_required(login_url='sign_in')
def invites_list_profiles_view(request):  
    
    template, context = list_relation_receiver_and_sender(request)
    context.update(
        {
            'page': 'list_not_friends',
            'start_animation': 'my_network'
        }
    )
    
    return render(request, template, context)


@login_required(login_url='sign_in')
def my_friends_invites_profiles_view1(request):
           
    template, context = list_relation_receiver_and_sender(request)
    context.update(
        {
            'page': 'my_friends',
            'start_animation': 'my_network'
        }
    )
    
    return render(request, template, context)


def send_invitation(request):
    if request.method == 'POST':
        pk = request.POST.get("profile_id")
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)
        
        relation = Relationship.objects.create(sender=sender, receiver=receiver, status="send")
        return redirect("my_network")
    return redirect('my_network')


def remove_from_friends(request):
    if request.method == 'POST':
        pk = request.POST.get("profile_id")
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)
        
        relation = Relationship.objects.get(
            (Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender))
        )
        relation.delete()
        return redirect("my_friends")
    return redirect('my_friends')

