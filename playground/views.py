from django.shortcuts import render
from django.http import HttpResponse
from playground.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
# Request---> Response
#Request handler
#in some fameworks it is called action
def home(request):
    #pull data from db
    #transform
    #send Email
  #  return HttpResponse({"THIS IS HOME PAGE"})
      return render(request,'index.html')

def about(request):
            return render(request,'about.html')

    #return HttpResponse({"THIS IS ABOUT PAGE"})
def categories(request):
              return render(request,'categories.html')

    #return HttpResponse({"THIS IS CATEGORIES PAGE"})
def contact(request):
              
             if request.method =='POST':
                     name=request.POST.get('name')
                     email=request.POST.get('email')
                     phone=request.POST.get('phone')
                     feedback=request.POST.get('feedback')
                     city=request.POST.get('city')
                     contact=Contact(name=name , email=email, phone=phone ,feedback=feedback, city=city, date=datetime.today())
                     contact.save()
                     messages.success(request, 'Your feedback is sent!')

             return render(request,'contact.html')

    #return HttpResponse({"THIS IS CONTACT PAGE"})