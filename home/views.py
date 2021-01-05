from django.shortcuts import render, HttpResponse
from home.models import Contact
from  home.forms import *
def homepage(request):
    context = {
        'name': 'Jhay Pace'
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
def contact(request):
    form = ContactForm()
    if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():
           form.save()
      
    context = {'form' : form}
    return render(request, 'contact.html' , context)
def project(request):
    return render(request, 'project.html')
def base(request):
    return render(request , 'base.html')