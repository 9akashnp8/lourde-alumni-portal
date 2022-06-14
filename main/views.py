from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from main.models import Alumni
from .forms import RegistrationForm, ContinueApplicationForm
import razorpay

#Helper functions
def createOrder():
    client = razorpay.Client(auth=("rzp_test_El7Ix2MLAjhhaV", "xBLuN8kFuD368XeUPIximvOJ"))
    client.set_app_details({"title" : "LMS Alumni Payment App", "version" : "0.1"})
    data = { "amount": 500, "currency": "INR", "receipt": "order_rcptid_11" }
    orderID = client.order.create(data=data)
    return orderID

def continue_application(email):
    alumni = Alumni.objects.get(email=email)
    if alumni.is_paid:
        return HttpResponse("You have completed your application")
    else:
        return redirect(regVerification, alumni.id)


# Create your views here.
def home(request):
    continue_form = ContinueApplicationForm()
    if request.method == 'POST':
        continue_form = ContinueApplicationForm(request.POST)
        if continue_form.is_valid():
            continue_application(continue_form.cleaned_data['email'])
    context = {'continue_form':continue_form}
    return render(request, 'home.html', context)

def register(request):
    form = RegistrationForm()
    continue_form = ContinueApplicationForm()
    if request.method == 'POST':
        if 'continue-application' in request.POST:
            continue_form = ContinueApplicationForm(request.POST)
            if continue_form.is_valid():
                continue_application(continue_form.cleaned_data['email'])
        if 'registration' in request.POST:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                try:
                    id = Alumni.objects.get(email=form.cleaned_data['email']).id
                    return redirect(regVerification, id)
                except Alumni.MultipleObjectsReturned:
                    return HttpResponse("You have already registered, check your application status here!")
    context = {'form':form, 'continue_form':continue_form}    
    return render(request, 'application/register-application.html', context)

def regVerification(request, id):
    continue_form = ContinueApplicationForm()
    if request.method == 'POST':
        if 'continue-application' in request.POST:
            continue_form = ContinueApplicationForm(request.POST)
            if continue_form.is_valid():
                continue_application(continue_form.cleaned_data['email'])

    alumni = Alumni.objects.get(id=id)
    orderID = createOrder()
    context = {'key_id': 'rzp_test_El7Ix2MLAjhhaV', 'order_id': orderID['id'], 'alumni':alumni, 'continue_form':continue_form}
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
            payment_id = payment_info['razorpay_payment_id'][0]
            order_id = payment_info['razorpay_order_id'][0]
            alumni.razor_payment_id = payment_id
            alumni.razor_order_id = order_id
            alumni.save()
        except KeyError:
            return HttpResponse("Payment failed, please try again!")
    return render(request, 'thankyou.html')