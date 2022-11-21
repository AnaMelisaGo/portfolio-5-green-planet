from django.shortcuts import render


def user_profile(request):
    """
    Function to show the user profile
    """
    template = 'profiles/profile.html'
    context = {}
    return render(request, template, context)
