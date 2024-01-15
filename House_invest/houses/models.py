from django.db import models


# Create your models here.
class Property_rent(models.Model):

    balcony = models.CharField(max_length=20, verbose_name="Պատշգամբ")
    parking = models.CharField(
        max_length=10, verbose_name="Կայանատեղի", blank=True, null=True)
    floor_area = models.CharField(max_length=10, verbose_name="Մակերես")
    lat = models.CharField(max_length=10, blank=True, null=True)
    construction_type = models.CharField(
        max_length=20, verbose_name="Շինության տիպ", blank=True, null=True)
    renovation = models.CharField(
        max_length=50, verbose_name="Վորանորոգում", blank=True, null=True)
    url = models.URLField(max_length=100)
    utility_payments = models.CharField(
        max_length=10, verbose_name="Կոմունալ վճարումներ", blank=True, null=True)
    furniture = models.CharField(
        max_length=10, verbose_name="Կահույք", blank=True, null=True)
    price = models.CharField(max_length=10)
    appliances = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, verbose_name="Նկարագիր")
    ceiling_height = models.CharField(max_length=10,
                                             verbose_name="Առաստաղի բարձրություն")
    floor = models.CharField(max_length=10, verbose_name="Հարկ")
    pets_allowed = models.CharField(
        max_length=5, blank=True, null=True)
    address = models.CharField(max_length=200)
    window_views = models.CharField(
        max_length=100, blank=True, null=True)
    prepayment = models.CharField(max_length=10, blank=True, null=True)
    new_construction = models.CharField(
        max_length=5, verbose_name="Նորակառույց", blank=True, null=True)
    rooms = models.CharField(
        max_length=10, verbose_name="Սենյակների քանակ")
    house_has = models.CharField(max_length=100, blank=True, null=True)
    title = models.TextField(max_length=1000)
    long = models.CharField(max_length=10, blank=True, null=True)
    amenities = models.CharField(max_length=100, blank=True, null=True)
    children_allowed = models.CharField(
        max_length=5, blank=True, null=True)
    floors_in_building = models.CharField(max_length=10,
                                     verbose_name="Հարկերի քանակ", blank=True, null=True)
    bathrooms = models.CharField(max_length=50,
                                             verbose_name="Սանհանգույցների քանակ")
    elevator = models.CharField(
        max_length=50, verbose_name="Վերելակ", blank=True, null=True)

    image = models.ImageField(blank=True, null=True, upload_to="rent_properties/", verbose_name="Image")

    def __str__(self):
        return f"Properties: {self.address}"



class Property_sale(models.Model):

    balcony = models.CharField(max_length=20, verbose_name="Պատշգամբ")
    parking = models.CharField(
        max_length=10, verbose_name="Կայանատեղի", blank=True, null=True)
    floor_area = models.CharField(max_length=10, verbose_name="Մակերես")
    lat = models.CharField(max_length=10, blank=True, null=True)
    construction_type = models.CharField(
        max_length=20, verbose_name="Շինության տիպ", blank=True, null=True)
    renovation = models.CharField(
        max_length=50, verbose_name="Վորանորոգում", blank=True, null=True)
    url = models.URLField(max_length=100)
    furniture = models.CharField(
        max_length=10, verbose_name="Կահույք", blank=True, null=True)
    price = models.CharField(max_length=10)
    appliances = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=500, verbose_name="Նկարագիր")
    ceiling_height = models.CharField(max_length=10,
                                             verbose_name="Առաստաղի բարձրություն")
    floor = models.CharField(max_length=10, verbose_name="Հարկ")
    address = models.CharField(max_length=200)
    window_views = models.CharField(
        max_length=100, blank=True, null=True)
    new_construction = models.CharField(
        max_length=5, verbose_name="Նորակառույց", blank=True, null=True)
    rooms = models.CharField(
        max_length=10, verbose_name="Սենյակների քանակ")
    house_has = models.CharField(max_length=100, blank=True, null=True)
    title = models.TextField(max_length=1000)
    long = models.CharField(max_length=10, blank=True, null=True)
    floors_in_building = models.CharField(max_length=10,
                                     verbose_name="Հարկերի քանակ", blank=True, null=True)
    bathrooms = models.CharField(max_length=50,
                                             verbose_name="Սանհանգույցների քանակ")
    elevator = models.CharField(
        max_length=50, verbose_name="Վերելակ", blank=True, null=True)

    image = models.ImageField(blank=True, null=True, upload_to="rent_properties/", verbose_name="Image")

    def __str__(self):
        return f"Properties: {self.address}"