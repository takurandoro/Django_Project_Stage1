from rest_framework import generics
from .models import City, Country
from .serializers import CountrySerializer, CitySerializer

# Create your views here.


class CountryCreateAPIView(generics.CreateAPIView):
    model = Country
    serializer_class = CountrySerializer


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailAPIView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_url_kwarg = "country_id"


class CountryUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_url_kwarg = "country_id"


class CountryDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_url_kwarg = "country_id"


class CityCreateAPIView(generics.CreateAPIView):
    model = City
    serializer_class = CitySerializer


class CityListAPIView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetailAPIView(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_url_kwarg = "city_id"


class CityUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_url_kwarg = "city_id"


class CityDeleteAPIView(generics.RetrieveDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_url_kwarg = "city_id"
