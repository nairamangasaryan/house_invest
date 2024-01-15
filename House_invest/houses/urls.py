"""House_invest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import home, Properties, RentProperties, SaleProperties, houses_list, single_house, contact_us, about_us

urlpatterns = [

    path('', home, name='home'),
    path("houses/", Properties.as_view(), name="houses"),
    path("rent-houses/", RentProperties.as_view(), name="rent-houses"),
    path("sale-houses/", SaleProperties.as_view(), name="sale-houses"),
    path("houses-list/", houses_list, name="houses-list"),
    path("single-house/", single_house, name="single-house"),
    path("contact/", contact_us, name="contact-us"),
    path("about/", about_us, name="about-us"),
]
