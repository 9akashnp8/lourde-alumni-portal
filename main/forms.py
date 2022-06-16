from django import forms
from django.forms import ModelForm
from .models import Alumni

class RegistrationForm(ModelForm):
    class Meta:
        model = Alumni
        fields = '__all__'
        exclude = ['application_no']
    
class GeneralSearchForm(forms.Form):
    email = forms.CharField(max_length=100)

