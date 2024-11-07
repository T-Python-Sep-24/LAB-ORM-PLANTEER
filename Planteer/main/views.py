from django.shortcuts import render, redirect
from django.http import HttpRequest
from plants.models import Plant
from .models import Contact
from .forms import ContactForm

#Home page
def homeView(request: HttpRequest):
    
    plants = Plant.objects.all()[0:3]

    return render(request ,'main/home.html', context={'plants':plants})

#Contact us page
def contactView(request: HttpRequest):
    contactData = ContactForm()

    response = render(request, 'main/contactUs.html')
    
    if request.method == "POST":
        contactData = ContactForm(request.POST)
        if contactData.is_valid():
            contactData.save()

        response = redirect('main:homeView') 

    return response

#All messages page
def allMessagesView(request: HttpRequest):
    messages = Contact.objects.all().order_by("-createdAt")
    response = render(request, 'main/allMessages.html')

    return response

#Mode change
def modeView(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    
    if mode == "light":
        response.set_cookie("mode", "light")
    elif mode == "dark":
        response.set_cookie("mode", "dark")
        
    return response

#Handling wrong entry
def notFoundView(request: HttpRequest):
    
    return render(request, '404.html')