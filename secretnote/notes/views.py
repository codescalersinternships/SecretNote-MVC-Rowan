from django.shortcuts import render

from .models import Note

def notes(request):
    notes_list = Note.objects.all().order_by('-creation_date')
    return render(request,'notes/notes.html',{'notes': notes_list})

