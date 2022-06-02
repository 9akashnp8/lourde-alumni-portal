import razorpay
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .forms import RegistrationForm

client = razorpay.Client(auth=("rzp_live_lf0bv0XHtSh7so","RNzB8Brxh6WAL7Rv2HAvNfH8"))

#Confirmation Email
SUBJECT = f"Welcome to the family {name}! You have successfully registered as an LMS Alumni"
MESSAGE = "Hello {name}, thank you for being a part of our family."

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    form = RegistrationForm
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            payment_url = "https://pages.razorpay.com/pl_JbXTzuuJU9gcsA/view?"
            return redirect(f"{payment_url}email={email}&name={name}")

    context = {'form':form}    
    return render(request, 'register.html', context=context)