from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='payment'),
    path('webhook/', views.webhook, name='webhook')
]