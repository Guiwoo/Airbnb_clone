from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as users_models

# Create your models here.


class Room(core_models.TimeStampedModel):
    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedroomss = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.Aggregate(default=False)
    host = models.ForeignKey(users_models.User, on_delete=models.CASCADE)
