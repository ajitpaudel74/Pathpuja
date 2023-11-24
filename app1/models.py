from django.db import models

# Create your models here.
class Puja(models.Model):
    name = models.CharField(max_length=30,null=True)
    desc = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.name

class Pandit(models.Model):
    name = models.CharField(max_length=30,null=True)
    #education=models.CharField(max_length=30)
    skills = models.ManyToManyField(Puja)
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.name