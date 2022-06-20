from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from main.models import Alumni
from .forms import *
import razorpay
from .sg_helper import applicationEmail, alumniEmail
from environs import Env

env = Env()
env.read_env()

#Helper functions
def createOrder():
    client = razorpay.Client(auth=(env.str("RAZORPAY_ID"), env.str("RAZORPAY_SECRET")))
    client.set_app_details({"title" : "LMS Alumni Payment App", "version" : "0.1"})
    data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
    orderID = client.order.create(data=data)
    return orderID



# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            applicant = Alumni.objects.get(email=form.cleaned_data['email'])
            applicationEmail(
                email=applicant.email,
                name=applicant.name,
                application_no=applicant.application_no,
                url=f'http:127.0.0.1:8000/verify/{applicant.id}'
            )
            return redirect(regVerification, applicant.id)
    context = {'form':form}    
    return render(request, 'application/register-application.html', context)

def regVerification(request, id):
    alumni = Alumni.objects.get(id=id)
    if alumni.is_paid:
        context = {'alumni':alumni}
        return render(request, 'application/alumni-paid.html', context) 
    orderID = createOrder()
    context = {'key_id': env.str("RAZORPAY_ID"), 'order_id': orderID['id'], 'alumni':alumni}
    return render(request, 'application/register-verify.html', context)

def regEdit(request, id):
    instance = Alumni.objects.get(id=id)
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            id = Alumni.objects.get(email=form.cleaned_data['email']).id
            return redirect(regVerification, id)
        
    context = {'form':form, 'instance':instance}
    return render(request, 'application/register-application.html', context)

@csrf_exempt
def thankyou(request, id):
    alumni = Alumni.objects.get(id=id)
    if request.method == 'POST':
        try:
            payment_info = dict(request.POST)
            alumni.razor_payment_id = payment_info['razorpay_payment_id'][0]
            alumni.razor_order_id = payment_info['razorpay_order_id'][0]
            alumni.save()
            alumniEmail(
                email=alumni.email,
                name=alumni.name,
                alumni_no=alumni.alumni_no
            )
        except KeyError:
            return HttpResponse("Payment failed, please try again!")
    context = {'alumni':alumni}
    return render(request, 'thankyou.html', context)

def search(request):
    return render(request, 'application/search.html')

def searchResults(request):
    email = request.POST.get('email')
    try:
        result = Alumni.objects.get(email=email)
    except Alumni.DoesNotExist:
        return render(request, 'partials/invalid-search.html')
    if result.is_paid:
        context = {'alumni':result}
        return render(request, 'partials/alumni-info.html', context)
    else:
        context = {'applicant':result}
        return render(request, 'partials/application-info.html', context)

    