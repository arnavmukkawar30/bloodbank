from datetime import datetime
from urllib.request import Request
from django.shortcuts import render,redirect,HttpResponse
# from django.http import HttpResponse
from home.models import Patient
from home.models import Donor
from home.models import Feedback
# FOR LOGIN AND LOGOUT 

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import CreateUserForm
from django.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'homepage.html')

@login_required(login_url='login')
def patient(request):
    if request.method == "POST":
        FName = request.POST.get('FName')
        LName = request.POST.get('LName')
        Address = request.POST.get('Address')
        PNumber = request.POST.get('PNumber')
        Reason = request.POST.get('Reason')
        Bloodgroup = request.POST.get('Bloodgroup')
        Unit = request.POST.get('Unit')
        patient = Patient(FName=FName, LName=LName, Address=Address,PNumber=PNumber,Reason=Reason,Bloodgroup=Bloodgroup,Unit=Unit,date=datetime.now())
        patient.save()
        return redirect('prequested')
    return render(request, 'patient.html')

@login_required(login_url='login')
def donor(request):
    if request.method == "POST":
        FName = request.POST.get('FName')
        LName = request.POST.get('LName')
        Address = request.POST.get('Address')
        PNumber = request.POST.get('PNumber')
        Disease = request.POST.get('Disease')
        Bloodgroup = request.POST.get('Bloodgroup')
        Unit = request.POST.get('Unit')
        donor = Donor(FName=FName, LName=LName, Address=Address,PNumber=PNumber,Disease=Disease,Bloodgroup=Bloodgroup,Unit=Unit,date=datetime.now())
        donor.save()
        return redirect('ddonated')
    return render(request, 'donor.html')


def loginpage(request): 
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            #authenticate user

            user = authenticate(request, username=username, password=password)

            if user is not None :
                login(request, user)
                return redirect('home')
            else :
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    return redirect('login')


def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:    
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Created successfully for '+ user)
                return redirect('login')
        context = {'form':form}
        return render(request, 'register.html',context)

def prequested(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        prequested = Feedback(name=name, email=email, message=message,date=datetime.now())
        prequested.save()
        return redirect('home')
    return render(request, 'prequested.html')

def ddonated(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        ddonated = Feedback(name=name, email=email, message=message,date=datetime.now())
        ddonated.save()  
        return redirect('home')  
    return render(request, 'ddonated.html')