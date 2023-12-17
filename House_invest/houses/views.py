from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")


def houses(request):
    return render(request, "houses.html")


def houses_list(request):
    return render(request, "houses-list.html")


def single_house(request):
    return render(request, "single-house.html")

def contact_us(request):
    return render(request, "contact-us.html")

def about_us(request):
    return render(request, "about-us.html")