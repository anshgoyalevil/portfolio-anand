from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage (/)")
    return render(request,'home.html')
def about(request):
    #return HttpResponse("This is my about page (/)")
    return render(request,'about.html')
def projects(request):
    #return HttpResponse("This is my project page (/)")
    return render(request,'projects.html')
def contact(request):
    if request.method=="POST":
        print("this is post")
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        ins = Contact(name=name, email=email, desc=desc)
        ins.save()
    # return HttpResponse("This is my contact page (/)")
    return render(request,'contact.html')