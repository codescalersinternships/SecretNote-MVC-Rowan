from django.shortcuts import get_object_or_404, render

from .models import Note

def notes(request):
    notes_list = Note.objects.all().order_by('-creation_date')
    return render(request,'notes/notes.html',{'notes': notes_list})

def note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request,'notes/note.html' ,{"note": note})
