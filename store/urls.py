from django.urls import path
from . import views

urlpatterns = [
    path('all_stores/', views.all_stores, name='all_stores'),
    path('<int:store_id>/', views.store_detail, name='store_detail'),
    path('add_store/', views.add_store, name='add_store'),
    path('edit_store/<int:store_id>/', views.edit_store, name='edit_store'),
]
