from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [
    path("switch/<int:pk>", views.switch_likes, name="favRoom"),
    path("favs/", views.SeeFavsView.as_view(), name="favs"),
]
