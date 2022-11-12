from django.shortcuts import render


def index(request):
    """
    To render home page
    """
    context = {
        'home': 'active',
    }
    return render(request, 'home/index.html', context)


def terms(request):
    """
    To render terms of use page
    """
    return render(request, 'home/terms.html')


def privacy(request):
    """
    To render privacy page
    """
    return render(request, 'home/privacy.html')