from django.shortcuts import render


def index(request):
    """
    To render home page
    """
    return render(request, 'home/index.html')
