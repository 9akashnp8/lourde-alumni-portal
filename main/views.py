from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from main.models import Alumni
from .forms import *
import razorpay

#Helper functions
def createOrder():
    client = razorpay.Client(auth=("rzp_test_El7Ix2MLAjhhaV", "xBLuN8kFuD368XeUPIximvOJ"))
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
            try:
                id = Alumni.objects.get(email=form.cleaned_data['email']).id
                return redirect(regVerification, id)
            except Alumni.MultipleObjectsReturned:
                return HttpResponse("You have already registered, check your application status here!")
    context = {'form':form}    
    return render(request, 'application/register-application.html', context)

def regVerification(request, id):
    alumni = Alumni.objects.get(id=id)
    orderID = createOrder()
    context = {'key_id': 'rzp_test_El7Ix2MLAjhhaV', 'order_id': orderID['id'], 'alumni':alumni}
    return render(request, 'application/register-verify.html', context)

def regEdit(request, id):
    instance = Alumni.objects.get(id=id)
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(regVerification, instance.id)
        
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
        except KeyError:
            return HttpResponse("Payment failed, please try again!")
    context = {'alumni':alumni}
    return render(request, 'thankyou.html', context)

def getApplicationStatus(request):
    form = GeneralSearchForm()
    if request.method == "POST":
        form = GeneralSearchForm(request.POST)
        if form.is_valid():
            result = Alumni.objects.get(email=form.cleaned_data['email'])
            return redirect(application, result.id)
    context = {'form':form}
    return render(request, 'application/search.html', context)

def getApplicationNumber(request):
    form = GeneralSearchForm()
    if request.method == "POST":
        form = GeneralSearchForm(request.POST)
        if form.is_valid():
            result = Alumni.objects.get(email=form.cleaned_data['email'])
            return redirect(application, result.id)
    context={'form':form}
    return render(request, 'application/search.html', context)

def getAlumniNumber(request):
    form = GeneralSearchForm()
    if request.method == "POST":
        form = GeneralSearchForm(request.POST)
        if form.is_valid():
            result = Alumni.objects.get(email=form.cleaned_data['email'])
            return redirect(alumniProfile, result.id)
    context = {'form':form}
    return render(request, 'application/search.html', context)

def getAlumniStatus(request):
    return render(request, 'application/search.html')

def application(request, id):
    result = Alumni.objects.get(id=id)
    return HttpResponse(f"Hello {result.name}")

def alumniProfile(request, id):
    result = Alumni.objects.get(id=id)
    if result.is_paid:
        return HttpResponse(f"Your alumni no: {result.alumni_no}")
    else:
        return HttpResponse("You have not paid, click here to continue application")

def searchResults(request):
    email = request.POST.get('email')
    result = Alumni.objects.get(email=email)
    context = {'result':result}
    return render(request, 'partials/search-results.html', context)

    