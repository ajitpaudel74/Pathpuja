from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
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

def loginUser(request):

    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Username or Password not correct.")

    return render(request,"login.html")

def logoutUser(request):
    logout(request)

    return redirect("login")

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
            user = form.cleaned_data.get('username')
            messages.success(request,"User has been created for "+user)
            return redirect("login")

    return render(request,"register.html",context)

