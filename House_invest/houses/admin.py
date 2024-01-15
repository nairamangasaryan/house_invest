from django.contrib import admin
from .models import Property_rent, Property_sale

# Register your models here.


@admin.register(Property_rent)
class Property_rentAdmin(admin.ModelAdmin):
    list_display = ('address',)


@admin.register(Property_sale)
class Property_saleAdmin(admin.ModelAdmin):
    list_display = ('address',)
