from django.shortcuts import render
#from django.http import HttpResponse
from server.models import Userreg;
from django.contrib import messages;
# Create your views here.

def home(request):
    if request.method=='POST':
        if request.POST.get('phone') and request.POST.get('password') and request.POST.get('dob'):
            saverecord=Userreg()
            saverecord.phone=request.POST.get('phone')
            saverecord.password=request.POST.get('password')
            saverecord.dob=request.POST.get('dob')
            saverecord.save()
            messages.success(request,"Registration successful")
            return render(request,'index.html')
        else:
            return render(request,'index.html')