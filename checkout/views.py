from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import TransactionForm
from .models import Transaction, OrderItem
from store.models import Store
from bag.contexts import bag_contents

import stripe


def checkout(request):
    """
    To render the checkout form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }
        transaction_form = TransactionForm(form_data)
        if transaction_form.is_valid():
            order = transaction_form.save()
            for item_id, item_data in bag.items():
                try:
                    store = Store.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            store=store,
                            quantity=item_data,
                        )
                        order_item.save()
                except Store.DoesNotExist:
                    messages.error(request, (
                        "An error has been detected."
                        "One of the items is not found."
                        "Please contact us for more info.")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))
            # Save user info into the profile
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.transaction_number]))
        else:
            messages.error(request, ('Error in the form. '
                                     'Please double check your information.'))
    else:
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


def checkout_success(request, transaction_number):
    """
    To handle success checkout
    """
    save_info = request.session.get('save_info')
    transaction = get_object_or_404(
        Transaction, transaction_number=transaction_number
    )

    messages.success(request, f'Order successfully processed! \
        Your order number is {transaction_number}. A confirmation \
        email will be sent to {transaction.email}.')

    if 'bag' in request.session:
        del request.session['bag']

    template = 'checkout/checkout_success.html'
    context = {
        'transaction': transaction,
    }

    return render(request, template, context)
