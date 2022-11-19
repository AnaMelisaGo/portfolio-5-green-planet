from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import TransactionForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    """
    To render the checkout form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'No contents in the bag.')
        return redirect(reverse('all_stores'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    
    transaction_form = TransactionForm()

    if not stripe_public_key:
        messages.warning(request, 'Public key is missing. \
            Are you sure you set it in your environment?')
    template = 'checkout/checkout.html'
    context = {
        'transaction_form': transaction_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }
    return render(request, template, context)
