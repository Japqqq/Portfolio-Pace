from django.shortcuts import render, HttpResponse
from home.models import Contact

def homepage(request):
    context = {
        'name': 'Jhay Pace'
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        TA = request.POST['desc']
        print(name,email,TA)
        ins = Contact(name = name , email = email , TA = TA)
        ins.save()
    return render(request, 'contact.html')
def project(request):
    return render(request, 'project.html')
def base(request):
    return render(request , 'base.html')