from django.http import HttpResponse
from django.shortcuts import render
from urdu.models import School
from urdu.models import madarsa
from urdu.models import contact
from . import views


# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
   return render(request, 'index.html')

def contact(request):
   return render(request, 'contact.html')

             
def form(request):
   d = ""
   if request.method == "POST":
      name = request.POST.get('name')
      email = request.POST.get('email')
      data=contact(name=name,email=email)
      d='check'
      data.save()
   return render(request, 'form.html',{
                           'd':d
                           })
              
def view(request):
   return render(request, 'view.html')
                    
                 
       
      
    