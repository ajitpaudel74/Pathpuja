from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *


# Create your views here.

def home(request):
    return render(request,'home.html')

def puja_list(request):
    pujas = Puja.objects.all()
    context={
        'pujas':pujas
    }

    return render(request,"puja_list.html",context)

def puja(request,pk):
    pandits = Pandit.objects.filter(skills=pk)
    puja = Puja.objects.get(id=pk)
    context={
        'pandits':pandits,
        'puja':puja
    }
    return render(request,"puja.html",context)

def login(request):

    return render(request,"login.html")

def register(request):
    form = RegistrationForm()
    context = {
        'form' : form,
        'errors':form.errors
    }

    if request.method=="POST":
        form=RegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/login")

    return render(request,"register.html",context)

