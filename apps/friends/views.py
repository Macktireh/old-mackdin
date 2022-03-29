from django.shortcuts import render
from django.contrib.auth import get_user_model

User = get_user_model()
from apps.friends.models import Relationship
from apps.profiles.models import Profile


def invites_received_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    # qs = Relationship.objects.invatation_received(profile)
    
    template = 'friends/invites.html'
    context = {
        # 'qs': qs,
    }
    
    return render(request, template, context)
