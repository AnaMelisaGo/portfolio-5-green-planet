from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Store, BusinessType
from .forms import StoreForm, BusinessTypeForm


# @required_login
# def add_favourite(request, store_id):
#     """
#     Add favourites to profile
#     """

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
                messages.error(request, 'You did not enter anything.')
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


@login_required
def add_business_type(request):
    """
    Add new business type for the store
    """
    business_type = BusinessType.objects.all()
    if not request.user.is_superuser:
        messages.error(request, 'RESTRICTED PAGE! Only staff members\
             can access this page. Sorry!')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = BusinessTypeForm(request.POST)
        if form.is_valid:
            form.save()
            messages.info(request, 'Successfully added')
            form = BusinessTypeForm()
        else:
            messages.error(request, 'Error! Make sure the form is\
                valid before you click the button.')
    else:
        form = BusinessTypeForm()
    template = 'stores/add_business_type.html'
    context = {
        'account': 'active',
        'form': form,
        'business_type': business_type,
    }
    return render(request, template, context)


@login_required
def edit_business_type(request, type_id):
    """
    Edit a business type
    """
    if not request.user.is_superuser:
        messages.error(request, 'RESTRICTED PAGE! Only staff members\
             can access this page. Sorry!')
        return redirect(reverse('home'))
    business_type = BusinessType.objects.all()
    btype = get_object_or_404(BusinessType, pk=type_id)
    if request.method == 'POST':
        form = BusinessTypeForm(request.POST, instance=btype)
        if form.is_valid():
            form.save()
            messages.info(request, 'You  have updated successfully!')
            return redirect(reverse('add_business_type'))
        else:
            messages.error(request,
                           ('Update error. '
                            'Please make sure the form is valid.'))
    else:
        form = BusinessTypeForm(instance=btype)
        messages.warning(request, f'You are updating {btype.friendly_name}')

    template = 'stores/edit_business_type.html'
    context = {
        'account': 'active',
        'form': form,
        'business_type': business_type,
        'btype': btype,

    }
    return render(request, template, context)


@login_required
def delete_business_type(request, type_id):
    """
    Delete business type for the store
    """
    type = get_object_or_404(BusinessType, pk=type_id)
    type.delete()
    return redirect('add_business_type')


@login_required
def add_store(request):
    """
    Add new store for users to purchase food or goods
    """
    if not request.user.is_superuser:
        messages.error(request, 'RESTRICTED PAGE! Only staff members\
             can access this page. Sorry!')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES)
        if form.is_valid:
            store = form.save()
            messages.info(request, 'Success! A new store is added.')
            return redirect(reverse('store_detail', args=[store.id]))
        else:
            messages.error(request, 'Failed to add store. Make sure the \
                 form is valid before you click "Add Store" button.')
    else:
        form = StoreForm()
    template = 'stores/add_store.html'
    context = {
        'account': 'active',
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_store(request, store_id):
    """
    Edit a store
    """
    if not request.user.is_superuser:
        messages.error(request, 'RESTRICTED PAGE! Only staff members\
             can access this page. Sorry!')
        return redirect(reverse('home'))
    store = get_object_or_404(Store, pk=store_id)
    if request.method == 'POST':
        form = StoreForm(request.POST, request.FILES, instance=store)
        if form.is_valid():
            form.save()
            messages.info(request, 'You  have updated this store!')
            return redirect(reverse('store_detail', args=[store.id]))
        else:
            messages.error(request,
                           ('Update error. '
                            'Please make sure the form is valid.'))
    else:
        form = StoreForm(instance=store)
        messages.warning(request, f'You are updating {store.store_name}')

    template = 'stores/edit_store.html'
    context = {
        'stores': 'active',
        'form': form,
        'store': store,

    }
    return render(request, template, context)


@login_required
def delete_store(request, store_id):
    """
    Delete a store from the webpage
    """
    if not request.user.is_superuser:
        messages.error(request, 'RESTRICTED PAGE! Only staff members\
             can access this page. Sorry!')
        return redirect(reverse('home'))
    store = get_object_or_404(Store, pk=store_id)
    store.delete()
    messages.info(request, 'Store deleted')
    return redirect(reverse('all_stores'))
