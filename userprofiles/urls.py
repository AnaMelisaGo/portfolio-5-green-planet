from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('view_history/', views.view_history, name='view_history'),
    path('transaction_history/<transaction_number>', views.transaction_history, name='transaction_history'),
]
