from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Note
from datetime import datetime


# @login_required
def notes(request):
    notes_list = Note.objects.all().order_by("-creation_date")
    return render(request, "notes/notes.html", {"notes": notes_list})


# @login_required
def note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    # print(datetime.now().day)
    # print(note.creation_date)
    note.view_count = note.view_count + 1
    print(note.view_count)
    note.save()
    if (
        note.view_count >= 10
        or note.creation_date.year < datetime.now().year
        or note.creation_date.month < datetime.now().month
        or note.creation_date.day < datetime.now().day
    ):
        return render(
            request,
            "notes/note.html",
            {"note": "", "date": note.creation_date, "current_date": datetime.now()},
        )
    if note.creation_date.hour < datetime.now().hour:
        return render(
            request,
            "notes/note.html",
            {"note": "", "date": note.creation_date, "current_date": datetime.now()},
        )

    return render(request, "notes/note.html", {"note": note})
