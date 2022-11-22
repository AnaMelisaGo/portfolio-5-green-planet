from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def user_profile(request):
    """
    Function to show the user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }
    return render(request, template, context)


def edit_profile(request):
    """
    Function to edit the user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=profile)
    transactions = profile.account.all()
    template = 'profiles/edit_profile.html'
    context = {
        'profile': profile,
        'form': form,
        'transactions': transactions,
    }
    return render(request, template, context)