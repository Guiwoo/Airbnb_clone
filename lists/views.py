from rooms import models as room_models
from django.views.generic import TemplateView
from . import models as lists_models
from django.shortcuts import redirect
from django.urls import reverse


def switch_likes(req, pk):
    action = req.GET.get("action", None)
    room = room_models.Room.objects.get_or_none(pk=pk)
    if room is not None and action is not None:
        the_list, _ = lists_models.List.objects.get_or_create(
            user=req.user, name="My Favorit Houses"
        )
        if action == "add":
            the_list.rooms.add(room)
        elif action == "remove":
            the_list.rooms.remove(room)
    return redirect(reverse("rooms:detail", kwargs={"pk": pk}))


class SeeFavsView(TemplateView):
    template_name = "lists/detail.html"
