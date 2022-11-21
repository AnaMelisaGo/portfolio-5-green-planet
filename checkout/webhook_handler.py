from django.http import HttpResponse

from .models import Transaction, OrderItem
from store.models import Store

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle any unexpected webhook event
        """
        return HttpResponse(
            content=f'Unexpected webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        transaction_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                transaction = Transaction.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                transaction_exists = True
                break
            except Transaction.DoesNOtExists:
                attempt += 1
                time.sleep(1)
        if transaction_exists:
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order',
                    status=200
                )
        else:
            transaction = None
            try:
                transaction = Transaction.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.load(bag).items():
                    store = Store.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            store=store,
                            quantity=item_data,
                        )
                        order_item.save()
            except Exception as e:
                if transaction:
                    transaction.delete()
                return HttpResponse(
                    content=f'Webhook received:\
                            {event["type"]} | ERROR: {e}',
                    status=500
                )

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
           Handle the payment_intent.payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
