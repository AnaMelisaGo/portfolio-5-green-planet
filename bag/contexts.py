def bag_content(request):
    """
    Context to be used for the entire website
    """
    bag_items = []
    grand_total = 0

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
    }
    return context