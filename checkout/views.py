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
        'stripe_public_key': 'pk_test_51LSarLAI6gj8NSENMJNRtzO0qqUAjA0PuMZpFne5zEPtdq51Et7CbI8FgklAdFoLVJ2xxPqwSTWpBCD5HOeMaqFa000xMo8U8h',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)
