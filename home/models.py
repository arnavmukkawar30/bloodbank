from email.mime import message
from django.db import models
from datetime import datetime

# Create your models here.
class Patient (models.Model):
    FName = models.CharField(max_length=20)
    LName = models.CharField(max_length=20)
    Address = models.TextField(blank=True)
    PNumber= models.IntegerField(default=0)
    Reason = models.TextField(blank=True)
    Bloodgroup = models.CharField(max_length=2)
    Unit= models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)
    def __str__(self):
        return self.FName + ' ' + self.LName + ' (' + self.Bloodgroup +')'

class Donor(models.Model):
    FName = models.CharField(max_length=20)
    LName = models.CharField(max_length=20)
    Address = models.TextField(blank=True)
    PNumber= models.IntegerField(default=0)
    Disease = models.TextField(blank=True)
    Bloodgroup = models.CharField(max_length=2)
    Unit= models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)
    def __str__(self):
        return self.FName + ' ' + self.LName + ' (' + self.Bloodgroup +')'

class Plogin(models.Model):
    USERNAME = models.CharField(max_length=20)
    PASSWORD = models.CharField( max_length=20)
    date = models.DateField(default=datetime.now)

class Feedback(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField( max_length=20)
    message = models.TextField(blank=True)
    date = models.DateField(default=datetime.now)
    def __str__(self):
        return self.name + ' feedback'