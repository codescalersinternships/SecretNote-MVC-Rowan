from django.shortcuts import get_object_or_404, redirect, render

from .models import Note
from datetime import datetime


def notes(request):
    notes_list = Note.objects.all().order_by("-creation_date")
    return render(request, "notes/notes.html", {"notes": notes_list})


def note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    print(datetime.now())
    print(note.creation_date)
    if note.creation_date.hour < datetime.now().hour:
        # note.delete()
        return render(request, "notes/note.html", {})
    # print(datetime.now())
    # print(note.creation_date)
    return render(request, "notes/note.html", {"note": note})
