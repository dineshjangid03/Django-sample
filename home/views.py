from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is aboutpage")

def service(request):
    return render(request, 'service.html')
    # return HttpResponse("this is servicepage")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name, email=email, phone=phone)
        contact.save()
    
    return render(request, 'contact.html')
    # return HttpResponse("this is contactpage")

def demo(request):
    data=Contact.objects.all()
    return render(request, 'demo.html', {'data':data})