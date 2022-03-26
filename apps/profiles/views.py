from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model

User = get_user_model()
from apps.profiles.models import Profile
from apps.profiles.forms import ProfileForm, UserProfileForm


def profile(request, pseudo):
    profile = get_object_or_404(Profile, pseudo=pseudo)
    profile.number_views = profile.number_views + 1
    profile.save()
    
    template = "profiles/profiles.html"
    context = {
        'profile': profile,
    }
    return render(request, template, context=context)

def update_profile(request):
    # profile = get_object_or_404(Profile, pseudo=pseudo)
    user = request.user
    
    user_profile_form = UserProfileForm(instance=user)
    profile_form = ProfileForm(instance=user.profile)
    
    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if profile_form.is_valid() and user_profile_form.is_valid():
            user_profile_form.save()
            # instance_user = user_profile_form.save(commit=False)
            # instance_user.email = request.user.email
            # instance_user.save()
            
            profile_form.save()
            # instance_profile = profile_form.save(commit=False)
            # instance_profile.user = request.user
            # instance_profile.save()
            
            # user_profile_form = UserProfileForm(instance=user)
            # profile_form = ProfileForm(instance=profile)
    
            return redirect('profile', pseudo=user.profile.pseudo)
            # return redirect('update_profile', pseudo=user.profile.pseudo)
    
    template = "profiles/update.html"
    context = {
        # 'profile': profile,
        'user_profile_form' : user_profile_form,
        'profile_form' : profile_form,
    }
    return render(request, template, context=context)
