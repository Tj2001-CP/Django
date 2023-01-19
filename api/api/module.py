from django.db import models

class CountryInfo(models.Model):
    flag_link = models.URLField()
    capital = models.CharField(max_length=255)
    largest_city = models.CharField(max_length=255)
    official_languages = models.CharField(max_length=255)
    area_total = models.CharField(max_length=255)
    population = models.CharField(max_length=255)
    GDP_nominal = models.CharField(max_length=255)#check
