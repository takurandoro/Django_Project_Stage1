from django.urls import path
from .views import *

urlpatterns = [
    path("countries/create/", CountryCreateAPIView.as_view(), name ="add_country"),
    path("countries/", CountryListAPIView.as_view(), name ="view_countries"),
    path("countries/<int:country_id>", CountryDetailAPIView.as_view(), name ="view_country"),
    path("countries/update/<int:country_id>", CountryUpdateAPIView.as_view(), name ="edit_country"),
    path("countries/delete/<int:country_id>", CountryDeleteAPIView.as_view(), name ="delete_country"),
    path("cities/create/", CityCreateAPIView.as_view(), name ="add_city"),
    path("cities/", CityListAPIView.as_view(), name ="view_cities"),
    path("cities/<int:city_id>", CityDetailAPIView.as_view(), name ="view_city"),
    path("cities/update/<int:city_id>", CityUpdateAPIView.as_view(), name ="edit_city"),
    path("cities/delete/<int:city_id>", CityDeleteAPIView.as_view(), name ="delete_city"),
]
