from django.shortcuts import render_to_response
from .models import *
import json
from django.conf import settings

import django_filters


class PropertyFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter(lookup_type='lt')
    bedrooms = django_filters.NumberFilter(lookup_type='gt')
    bathrooms = django_filters.NumberFilter(lookup_type='gt')

    class Meta:
        model = Property
        fields = ['price', 'bedrooms', 'bathrooms']
        order_by = ['price', 'bedrooms']


def search(request):
    file = open(settings.BASE_DIR + '/houses/IslandRentals.json')
    data = json.load(file)
    file.close()
    data = data['property']
    for house in data:
        if 'address' in house:
            address = house['address']
            if Property.objects.filter(address=address):
                print("Property already in db")
            else:
                size = house['size']
                property = Property.objects.create(address=address, price=house.get('price', 'no price'), bedrooms=size.get('num_bedrooms', 0),
                                                   bathrooms=size.get('num_bathrooms', 0), sq_feet=size.get('sq_ft', 0), lot_sq_feet=size.get('lot_sq_ft', 0),
                                                   proximity_to_volcanoe=house.get('proximity_to_volcanoe', 0), school_rating=house.get('school_rating', 0),
                                                   distance_to_bar=house.get('distance_to_bar', 0), image_url=house.get('image', 'no image available'),
                                                   home_type=house.get('home_type', 'no type'), distance_to_public_transit=house.get('distance_to_public_transit', 0))
                property.save
    f = PropertyFilter(request.GET, queryset=Property.objects.all())
    return render_to_response('search/search.html', {'filter': f})
