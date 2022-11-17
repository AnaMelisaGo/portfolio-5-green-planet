import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from store.models import Store


class Transaction(models.Model):
    """
    Transaction model to purchase food
    from selected store
    """
    transaction_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)

    def _generate_transaction_num(self):
        """
        Generate a random, unique number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total
        """
        self.grand_total = self.orderitem.aggregate(
            Sum('orderitem_order_total'))['orderitem_order_total__sum']
        self.save()

    def save(self, *args, **kwargs):
        """
        To override the save method when order number is not set
        """
        if not self.transaction_number:
            self.transaction_number = self._generate_transaction_num()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.transaction_number


class OrderItem(models.Model):
    """
    Inline order list
    """
    order = models.ForeignKey(Transaction, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='orderitem')
    store = models.ForeignKey(Store, null=False, blank=False,
                              on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    order_total = models.DecimalField(max_digits=6, decimal_places=2,
                                      null=False, blank=False,
                                      editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method by setting the lineitem total
        and update the order total.
        """
        self.order_total = self.store.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.store.store_name} with {self.transaction.transaction_number}'
