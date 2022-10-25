from datetime import datetime
# import email
from unicodedata import name
from django.shortcuts import render,HttpResponse
from home.models import contact
from django.contrib import messages

# Create your views here.
def index(request):

    return render(request,"index.html")

def marriage(request):

    return render(request,"marriage.html")
def backgrounds(request):

    return render(request,"backgrounds.html")
def haldhi(request):

    return render(request,"haldhi.html")
def first_night(request):

    return render(request,"first_night.html")
def house(request):

    return render(request,"house.html")
def jd(request):
    return render(request,'jd.html')

def about(request):
    return render(request,"about.html")
def success(request):
    return render(request,"success.html")

def Contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        pid=request.POST.get('pid')
        Contact=contact(name=name,mobile=mobile,pid=pid,date=datetime.today())
        Contact.save()
        messages.success(request, 'Your message has been sent.')



    return render(request,"contact.html")
