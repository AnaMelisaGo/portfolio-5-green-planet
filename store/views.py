from django.shortcuts import render
from .models import Store


def all_stores(request):
    """
    To view all stores
    """
    stores = Store.objects.all()

    context = {
        'store': 'active',
        'all_stores': 'active',
        'stores': stores,
    }
    return render(request, 'stores/all_stores.html', context)
