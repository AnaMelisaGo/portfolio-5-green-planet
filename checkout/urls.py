from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('payment/', views.checkout, name='checkout'),
    path('checkout_user', views.checkout_user, name='checkout_user'),
    path(
        'checkout_success/<transaction_number>',
        views.checkout_success,
        name='checkout_success'
    ),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
    ),
    path('wh/', webhook, name='webhook'),
]
