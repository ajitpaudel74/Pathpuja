from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login,logout
from .models import *
from .forms import RegistrationForm,BookingForm


def home(request):
    pandits=Pandit.objects.all()
    context={
        'pandits':pandits
    }
    return render(request,'home.html',context)

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

    return redirect("home")

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


def BookPandit(request, pk,pdt):
    pandit = Pandit.objects.get(id=pdt)
    puja=Puja.objects.get(id=pk)
    if request.method=="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            book=form.save(commit=False)
            book.user=request.user
            book.pandit=pandit
            book.puja=puja
            book.save()
            Availability.objects.create(
                pandit=pandit,
                date=book.date,
                booking=book
            )
            return redirect("/")
        else:
            print(form.errors)

    else:
        skills= pandit.skills.first()
        booking_instance = Booking(user=request.user,pandit=pandit,puja=puja)
        form=BookingForm(instance=booking_instance)

    context={
        'form':form,
        'pandit':pandit,
        'puja':puja,
        'user':request.user
    }
    return render(request,"booking.html",context)


def panditProfile(request,pk):
    pandit=Pandit.objects.get(id=pk)
    skills = pandit.skills.all()
    context={
        'pandit':pandit,
        'skills':skills
    }
    return render(request,"pandit_profile.html",context)

def userProfile(request):
    user=request.user
    bookings=Booking.objects.filter(user=user)

    context={
        'user':user,
        'bookings':bookings
    }
    return render(request,"user_profile.html",context)

def cancelBooking(request,pk):
    booking=Booking.objects.get(id=pk)
    booking.delete()

    return redirect("user_profile")