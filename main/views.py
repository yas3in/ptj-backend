from django.shortcuts import render
import jdatetime


def index(request):
    emroz = jdatetime.datetime.today()
    return render(request, 'main/index.html', {'emroz': emroz.date()})


def aboutus(request):
    return render(request, "main/aboutus.html")


def contact(request):
    return render(request, "main/contact.html")


def service(request):
    return render(request, "404.html")
 
 
def authentication(request):
    return render(request, "main/authentication.html")     
 