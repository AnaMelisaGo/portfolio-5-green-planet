from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from .models import Store, BusinessType


def all_stores(request):
    """
    To view all stores
    """
    stores = Store.objects.all()
    query = None
    business_types = None
    sort = None
    direction = None

    if request.GET:
        # Sort
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'store_name':
                sortkey = 'lower_name'
                stores = stores.annotate(lower_name=Lower('store_name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            if sortkey == 'business_type':
                sortkey = 'business_type__name'
            stores = stores.order_by(sortkey)

        # Filter by category
        if 'business_type' in request.GET:
            business_types = request.GET['business_type']
            filter = Q(business_type__name__icontains=business_types)
            stores = stores.filter(filter)

        # Query for search bar
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter anything.")
                return redirect(reverse('all_stores'))
            queries = Q(store_name__icontains=query) | Q(
                details__icontains=query
            ) | Q(business_type__name__icontains=query)
            stores = stores.filter(queries)
    current_sorting = f'{sort}_{direction}'
    context = {
        'store': 'active',
        'all_stores': 'active',
        'stores': stores,
        'current_type': 'business_types',
        'current_sorting': current_sorting,
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
