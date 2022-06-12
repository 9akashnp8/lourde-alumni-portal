from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('registration-edit/<int:id>', views.regEdit, name='regEdit'),
    path('verify/<str:id>', views.regVerification, name='regVerification'),
    path('make-payment/<str:id>', views.payment, name='payment'),
    path('thank-you/', views.thankyou, name='thankyou'),
    path('webhook/', views.webhook, name='webhook')
]