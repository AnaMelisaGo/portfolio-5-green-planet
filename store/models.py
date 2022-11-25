from django.db import models
from django.contrib.auth.models import User


class BusinessType(models.Model):
    """
    Category model
    """
    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        """
        To return a string of value
        """
        return self.name

    def get_friendly_name(self):
        """
        Get friendly name
        """
        return self.friendly_name


class Store(models.Model):
    """
    Store Model
    """
    business_type = models.ForeignKey(
        'BusinessType', null=True, blank=True, on_delete=models.SET_NULL
    )
    store_name = models.CharField(max_length=255)
    details = models.TextField()
    address = models.CharField(max_length=255)
    original_price = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.DecimalField(
        max_digits=4, decimal_places=2, null=True, blank=True
    )
    favourites = models.ManyToManyField(
        User, related_name='favourite', default=None, blank=True
    )
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.store_name
