from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('business/', views.business, name='business'),
    path('faq/', views.faq_page, name='faq'),
]
