from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Alumni

class RegistrationForm(ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'
