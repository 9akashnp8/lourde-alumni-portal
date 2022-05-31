from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import RegistrationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    form = RegistrationForm
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}    
    return render(request, 'register.html', context=context)