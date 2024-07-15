from django.urls import path
from . import views

urlpatterns = [
    path("", views.notes, name="notes"),
    path("<note_id>/", views.note, name="note"),
]
