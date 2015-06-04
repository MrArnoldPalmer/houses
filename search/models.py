from django.db import models


class Property(models.Model):
    address = models.TextField(primary_key=True, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    bedrooms = models.IntegerField(default=0)
    bathrooms = models.DecimalField(default=0, max_digits=2, decimal_places=1)
    sq_feet = models.IntegerField(default=0)
    lot_sq_feet = models.IntegerField(default=0)
    proximity_to_volcanoe = models.IntegerField(default=0)
    school_rating = models.IntegerField(default=0)
    distance_to_bar = models.DecimalField(
        max_digits=3, decimal_places=2, default=0)
    image_url = models.CharField(max_length=200)
    home_type = models.CharField(max_length=200)
    distance_to_public_transit = models.DecimalField(
        max_digits=3, decimal_places=2, default=0)

    def create(cls, address, price, bedrooms,
               bathrooms, sq_feet, lot_sq_feet, proximity_to_volcanoe,
               school_rating, distance_to_bar, image_url,
               home_type, distance_to_public_transit):
        property = cls(address=address, price=price,
                       bedrooms=bedrooms, bathrooms=bathrooms,
                       sq_feet=sq_feet, lot_sq_feet=lot_sq_feet,
                       proximity_to_volcanoe=proximity_to_volcanoe,
                       school_rating=school_rating, distance_to_bar=distance_to_bar,
                       image_url=image_url, home_type=home_type,
                       distance_to_public_transit=distance_to_public_transit)
        return property

    def __str__(self):
        return self.address
