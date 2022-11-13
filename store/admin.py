from django.contrib import admin
from .models import Store, BusinessType


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'store_name',
        'business_type',
        'original_price',
        'price',
        'rating',
        'image',
    )

    ordering = ('store_name',)


class BusinessTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Store, StoreAdmin)
admin.site.register(BusinessType, BusinessTypeAdmin)
