from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from .models import Store, BusinessType


def all_stores(request):
    """
    To view all stores
    """
    stores = Store.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything.")
                return redirect(reverse('all_stores'))
            queries = Q(store_name__icontains=query) | Q(
                details__icontains=query
            ) | Q(business_type__name__icontains=query)
            stores = stores.filter(queries)

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
