from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .views import *
from .models import *
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

class BookingForm(ModelForm):
    class Meta:
        model=Booking
        fields = ['date']

    date= forms.DateField(
        label="Date Booked for",
        required=True,
        widget=forms.DateInput(attrs={"type": "date"}),
    )
