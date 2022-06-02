import razorpay
from django.shortcuts import redirect, render
from .forms import RegistrationForm

client = razorpay.Client(auth=("rzp_live_lf0bv0XHtSh7so","RNzB8Brxh6WAL7Rv2HAvNfH8"))
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
            # r = client.payment_link.create({
            #     "amount": 100,
            #     "currency": "INR",
            #     "accept_partial": False,
            #     "customer": {
            #         "name": form.cleaned_data["name"],
            #         "email": form.cleaned_data["email"],
            #         "contact": "+918075680338"
            #     },
            #     "notify": {
            #         "sms": True,
            #         "email": False,
            #     },
            #     "callback_url": "http://127.0.0.1",
            #     "callback_method": "get"
            # })
            # print(r)
            # return redirect(r["short_url"])

    context = {'form':form}    
    return render(request, 'register.html', context=context)