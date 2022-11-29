from django.shortcuts import get_object_or_404
from store.models import Store, BusinessType


def bag_contents(request):
    """
    Context to be used for the entire website
    """
    b_type = BusinessType.objects.all()
    bag_items = []
    grand_total = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        store = get_object_or_404(Store, pk=item_id)
        grand_total += quantity * store.price
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'store': store,
        })

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
        'b_type': b_type,
    }
    return context
