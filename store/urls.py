from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_stores, name='all_stores'),
    path(
        'detail_store/<int:store_id>/', views.store_detail, name='store_detail'
    ),
    path('add_store/', views.add_store, name='add_store'),
    path('edit_store/<int:store_id>/', views.edit_store, name='edit_store'),
    path(
        'delete_store/<int:store_id>/',
        views.delete_store,
        name='delete_store'
    ),
    path(
        'add_business_type/', views.add_business_type, name='add_business_type'
    ),
    path(
        'delete_business_type/<int:type_id>', views.delete_business_type, name='delete_business_type'
    ),
]
