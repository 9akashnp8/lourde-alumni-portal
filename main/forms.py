from xml.dom import ValidationErr
from django import forms
from django.forms import ModelForm, ValidationError
from .models import Alumni

class RegistrationForm(ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'
        exclude = ['application_no']
        error_messages = {
            'email': {
                'unique': ("You are already registered, check your application status from the top menu"),
            },
        }
class GeneralSearchForm(forms.Form):
    email = forms.CharField(max_length=100)

