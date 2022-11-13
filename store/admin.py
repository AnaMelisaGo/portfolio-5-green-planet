from django.contrib import admin
from .models import Store, Category


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'store_name',
        'category',
        'original_price',
        'price',
        'rating',
        'image',
    )

    ordering = ('store_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
