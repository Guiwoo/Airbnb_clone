from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.shortcuts import render
from django_countries import countries
from . import models


class HomeView(ListView):
    """Homeview Definition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class RoomDetail(DetailView):
    """RoomDetail Definition"""

    model = models.Room
    context_object_name = "room"


def search(req):
    city = req.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = req.GET.get("country", "KR")
    guests = int(req.GET.get("guests", 0))
    price = int(req.GET.get("price", 0))
    bedrooms = int(req.GET.get("bedrooms", 0))
    beds = int(req.GET.get("beds", 0))
    baths = int(req.GET.get("baths", 0))
    s_amenities = req.GET.getlist("amenities")
    s_facilities = req.GET.getlist("facilities")
    room_type = int(req.GET.get("room_type", 0))
    instant = bool(req.GET.get("instant", False))
    superhost = bool(req.GET.get("superhost", False))

    form = {
        "city": city,
        "s_country": country,
        "s_room_type": room_type,
        "guests": guests,
        "bedrooms": bedrooms,
        "price": price,
        "beds": beds,
        "baths": baths,
        "s_facilities": s_facilities,
        "s_amenities": s_amenities,
        "instant": instant,
        "superhost": superhost,
    }
    room_types = models.RoomType.objects.all()
    amenities = models.Amenity.objects.all()
    facilities = models.Facility.objects.all()

    choices = {
        "countries": countries,
        "room_types": room_types,
        "amenities": amenities,
        "facilities": facilities,
    }

    filter_args = {}

    if city != "Anywhere":
        filter_args["city__startswith"] = city

    filter_args["country"] = country

    if room_type != 0:
        filter_args["room_type__pk__exact"] = room_type

    if price != 0:
        filter_args["price__lte"] = price

    if guests != 0:
        filter_args["guests__gte"] = guests

    if bedrooms != 0:
        filter_args["bedrooms__gte"] = bedrooms

    if beds != 0:
        filter_args["beds__gte"] = beds

    if baths != 0:
        filter_args["baths__gte"] = baths

    if instant is True:
        filter_args["instant_book"] = True

    if superhost is True:
        filter_args["host__superhost"] = True

    if len(s_amenities) > 0:
        for s_amenity in s_amenities:
            filter_args["amenities__pk"] = int(s_amenity)

    if len(s_facilities) > 0:
        for s_facility in s_facilities:
            filter_args["fas_facilities__pk"] = int(s_facility)

    rooms = models.Room.objects.filter(**filter_args)

    return render(
        req,
        "rooms/search.html",
        {**form, **choices, "rooms": rooms},
    )
