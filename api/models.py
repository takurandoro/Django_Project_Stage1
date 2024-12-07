from django.db import models

# Create your models here.


class Country(models.Model):

    class ContinentType(models.TextChoices):
        AFRICA = "Africa", "Africa"
        EUROPE = "Europe", "Europe"
        AMERICA = "America", "America"
        ASIA = "Asia", "Asia"
        OCEANIA = "Oceania", "Oceania"

    name = models.CharField(max_length=100, unique=True)
    continent = models.CharField(max_length=50, choices=ContinentType.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="cities"
    )

    def __str__(self):
        return self.name
