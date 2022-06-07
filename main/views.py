from django.http import HttpResponse
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.core.mail import send_mail
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
            request.session['registered_data'] = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'batch': form.cleaned_data['batch'],
            }
            return HttpResponse("Registered")
            # payment_url = 'https://pages.razorpay.com/pl_JbXTzuuJU9gcsA/view?'
            # return redirect(f'{payment_url}email={email}&name={name}')

    context = {'form':form}    
    return render(request, 'register.html', context=context)

@csrf_exempt
def webhook(request):

    return HttpResponse('200')