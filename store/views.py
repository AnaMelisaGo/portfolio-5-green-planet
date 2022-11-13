from django.shortcuts import render, get_object_or_404
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


def store_detail(request, store_id):
    """
    To view a single store and its detail
    """
    store = get_object_or_404(Store, pk=store_id)

    context = {
        'stores': 'active',
        'store': store,
    }
    return render(request, 'stores/store_detail.html', context)
