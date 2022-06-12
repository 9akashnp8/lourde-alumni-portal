from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('registration-edit/<int:id>', views.regEdit, name='regEdit'),
    path('verify/<str:id>', views.regVerification, name='regVerification'),
    path('thank-you/<str:id>', views.thankyou, name='thankyou'),
]