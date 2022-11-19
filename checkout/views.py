from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import TransactionForm


def checkout(request):
    """
    To render the checkout form
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'No contents in the bag.')
        return redirect(reverse('all_stores'))

    transaction_form = TransactionForm()
    template = 'checkout/checkout.html'
    context = {
        'transaction_form': transaction_form,
    }
    return render(request, template, context)
