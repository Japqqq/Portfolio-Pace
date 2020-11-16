from django.shortcuts import render, HttpResponse


def homepage(request):
    context = {
        'name': 'Jhay Pace'
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def project(request):
    return render(request, 'project.html')