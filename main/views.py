from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')


def aboutus(request):
    return render(request, "main/aboutus.html")


def contact(request):
    return render(request, "main/contact.html")


def service(request):
    return render(request, "404.html")
