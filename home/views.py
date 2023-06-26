from django.shortcuts import render
from home.models import Contact,HomePage
# Create your views here.
def aboutus(request):
    contact = Contact.objects.all()
    home = HomePage.objects.all()
    context = {'contact':contact,'home':home}
    
    return render(request,'aboutus.html',context)


def contactus(request):
    contact = Contact.objects.all()
    home = HomePage.objects.all()
    context = {'contact':contact,'home':home}
    
    return render(request,'contact_us.html',context)