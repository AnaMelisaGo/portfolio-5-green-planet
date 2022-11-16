from django.shortcuts import render, redirect, HttpResponse


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
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        messages.error(request, 'This item is in the bag')
    else:
        bag[item_id] = quantity
    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def delete_item(request, item_id):
    """
    Delete an item from the bag page
    """

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
