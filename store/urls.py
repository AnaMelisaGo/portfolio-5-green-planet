from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_stores, name='all_stores'),
    path('<store_id>', views.store_detail, name='store_detail')
]
