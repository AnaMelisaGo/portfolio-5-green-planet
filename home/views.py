from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
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


def business(request):
    """
    To render page for business who wants to join
    """
    template = 'home/business.html'
    context = {
        'business': 'active',
    }
    return render(request, template, context)


def faq_page(request):
    """
    To render the frequently asked question page for users
    """
    template = 'home/faq.html'
    return render(request, template)
