from django.utils import timezone
from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse
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


def room_detail(requset, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(requset, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
