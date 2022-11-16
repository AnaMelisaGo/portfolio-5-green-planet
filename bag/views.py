from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from store.models import Store


def view_bag(request):
    """
    To render shopping bag
    """
    context = {
        'bag': 'bag-active',
    }
    return render(request, 'bag/bag.html', context)


def add_item(request, item_id):
    """
    Add item to bag
    """
    store = get_object_or_404(Store, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        messages.error(
            request, 'This item is in the bag already.' +
            ' Only one bag can be purchased. Sorry for the inconvinience!'
        )
    else:
        bag[item_id] = quantity
        messages.success(request, f'You added {store.store_name} to the bag')
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def delete_item(request, item_id):
    """
    Delete an item from the bag page
    """

    try:
        store = get_object_or_404(Store, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Deleted {store.store_name} from the bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error occured: {e}')
        return HttpResponse(status=500)
