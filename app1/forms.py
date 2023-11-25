from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .views import *
from .models import *

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

class BookingForm(ModelForm):
    class Meta:
        model=Booking
        fields = '__all__'
        
        #to prefill the puja field in form

        # def __intit__(self, *args, **kwargs):
        #     super().__init__(**args, **kwargs)#calls constructor from parent class 'Modelform' to ensure form is properly
        #                                     # initialized with necessary arguments

        #     initial = kwargs.get('initial') #gets the initial dictionary passed in views.py form
        #     if initial:#if initial dict has value
        #         skills = initial.get('skills')#get the skills value
        #         if skills:
        #             self.fields['puja'].initial = skills#prefill the skills field in form with skills value
