from django.shortcuts import render


def view_bag(request):
    """
    To render shopping bag
    """
    context = {
        'bag': 'bag-active',
    }
    return render(request, 'bag/bag.html', context)