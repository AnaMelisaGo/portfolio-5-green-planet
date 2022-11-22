from django.contrib import admin
from .models import Transaction, OrderItem


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order_total',)


class TransactionAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('transaction_number', 'date',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    fields = ('transaction_number', 'user_profile', 'date', 'full_name',
              'email', 'phone_number', 'grand_total',
              'original_bag', 'stripe_pid',)

    list_display = ('transaction_number', 'date', 'full_name',
                    'grand_total',)

    ordering = ('-date',)


admin.site.register(Transaction, TransactionAdmin)
