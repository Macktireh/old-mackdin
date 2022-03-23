from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()
from apps.profiles.models import Profile
from apps.profiles.forms import ProfileForm


def profile(request, pseudo):
    profile = get_object_or_404(User, first_name=pseudo)
    profile_form = ProfileForm()
    
    template = "profiles/profiles.html"
    context = {
        'Profiles': profile,
        'profile_form' : profile_form,
    }
    return render(request, template, context=context)
