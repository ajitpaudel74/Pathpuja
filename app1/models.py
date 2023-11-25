from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Puja(models.Model):
    name = models.CharField(max_length=30,null=True)
    desc = models.CharField(max_length=3000,null=True)

    def __str__(self):
        return self.name

class Pandit(models.Model):
    name = models.CharField(max_length=30,null=True)
    #education=models.CharField(max_length=30)
    skills = models.ManyToManyField(Puja)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    user= models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    pandit = models.ForeignKey(Pandit,null=True,on_delete=models.SET_NULL)
    puja = models.ForeignKey(Puja,null=True,on_delete=models.SET_NULL)
    date = models.DateField(("Book for date"), auto_now=False, auto_now_add=False)