from rest_framework import serializers
from .models import City, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ("name", "continent")


class CitySerializer(serializers.ModelSerializer):
    country = Country
    country_name = serializers.ReadOnlyField(source="country.name")

    class Meta:
        model = City
        fields = ("name", "country", "country_name")
        extra_kwargs = {
            "country": {"write_only": True},
        }
