from django.shortcuts import render


def index(request):
    """
    To render home page
    """
    context = {
        'home': 'active',
    }
    return render(request, 'home/index.html', context)
