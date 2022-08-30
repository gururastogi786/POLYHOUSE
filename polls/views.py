from dis import dis
from tkinter import Variable
from django.shortcuts import render,HttpResponse
from .models import *
from polls.models import signup


# Create your views here.
def index(request):
    # context = {
    #     "Variable1":"this is Anmol Rastogi",
    #     "Variable2":"this is shabnam "
    # }
    return render(request, 'index.html')
    # return HttpResponse("this is my home  page Anmol Rastogi")

def about(request):
    return render(request, 'about.html')

def signup(request):
    if request.method =="POST":
        name=request.POST.get("name")
        number=request.POST.get("number")
        State=request.POST.get("State")
        district=request.POST.get("district")
        village=request.POST.get("village")
        password=request.POST.get("password")
        c_pass=request.POST.get("c_pass")
        print(name, number, State,district,village,password,c_pass)

        obj = signup(name=name,number=number, State=State, district=district, village=village, password=password, c_pass=c_pass)
        obj.save()
    return render(request,'signup.html')
    

def services(request):
    return render(request,'services.html')


def contact(request):
    if request.method =="POST":
        name=request.POST.get("name")
        number=request.POST.get("number")
        # print(name,number)
        obj = contactUs(name=name,number=number)
        obj.save()
        
        
    return render(request,"contectUs.html")



