from django.shortcuts import render
from . import models


def all_rooms(req):
    all_room_data = models.Room.objects.all()
    return render(req, "rooms/home.html", context={"rooms": all_room_data})
