from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('' , views.homepage, name='home'),
    path('about' , views.about, name = 'about'),
    path('project' , views.project, name = 'project'),
    path('contact' , views.contact, name='contact'),
    path('base' , views.base, name='base')

    
]
