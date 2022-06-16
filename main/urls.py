from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('registration-edit/<int:id>', views.regEdit, name='regEdit'),
    path('verify/<str:id>', views.regVerification, name='regVerification'),
    path('thank-you/<str:id>', views.thankyou, name='thankyou'),

    path('get-application-status/', views.getApplicationStatus, name='getApplicationStatus'),
    path('get-application-number/', views.getApplicationNumber, name='getApplicationNumber'),
    path('get-alumni-number/', views.getAlumniNumber, name='getAlumniNumber'),
    path('get-alumni-status/', views.getAlumniStatus, name='getAlumniStatus'),
    path('application/<str:id>', views.application, name='application'),
    path('alumni/<str:id>', views.alumniProfile, name='alumniProfile'),
]