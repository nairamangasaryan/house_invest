from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from .models import Property_rent, Property_sale

# Create your views here.


def home(request):
    return render(request, "index.html")


class Properties(ListView):
    template_name="houses.html"
    model = Property_rent
    context_object_name="properties_rent"


class RentProperties(ListView):
    template_name="rent-houses.html"
    model = Property_rent
    context_object_name="properties_rent"

class SaleProperties(ListView):
    template_name="sale-houses.html"
    model = Property_sale
    context_object_name="properties_sale"




def houses_list(request):
    return render(request, "houses-list.html")


def single_house(request):
    return render(request, "single-house.html")

def contact_us(request):
    return render(request, "contact-us.html")

def about_us(request):
    return render(request, "about-us.html")