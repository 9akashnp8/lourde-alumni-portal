from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from main.models import Alumni
from .forms import RegistrationForm

#Confirmation Email
SUBJECT = 'Welcome to the family! You have successfully registered as an LMS Alumni'
MESSAGE = 'Hello {name}, thank you for being a part of our family.'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            id = Alumni.objects.get(email=form.cleaned_data['email']).id
            return redirect(regVerification, id)
            # payment_url = 'https://pages.razorpay.com/pl_JbXTzuuJU9gcsA/view?'
            # return redirect(f'{payment_url}email={email}&name={name}')
    context = {'form':form}    
    return render(request, 'register-application.html', context=context)

def regVerification(request, id):
    alumni = Alumni.objects.get(id=id)
    if request.method == 'POST':
        payment_url = 'https://pages.razorpay.com/pl_JbXTzuuJU9gcsA/view?'
        return redirect(f'{payment_url}email={alumni.email}&name={alumni.name}&phone={alumni.phone}')
    context = {'alumni':alumni}
    return render(request, 'register-verify.html', context)

def regEdit(request, id):
    instance = Alumni.objects.get(id=id)
    form = RegistrationForm(instance=instance)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(regVerification, instance.id)
        
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def webhook(request):

    return HttpResponse('200')