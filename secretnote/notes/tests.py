from django.test import Client, TestCase
from django.urls import reverse
from .models import Note
import datetime
from django.utils import timezone


class NoteViewNotesTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_note = Note.objects.create(title="Testing", content="hello from test")

    def test_notes_response_code(self):
        response = self.client.get(reverse("notes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/notes.html")

    def test_notes_response(self):

        response = self.client.get(reverse("notes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/notes.html")
        self.assertEqual(response.context["notes"][0], self.test_note)

    def test_single_note_response(self):
        url = reverse(
            "note",
            args=[
                self.test_note.id,
            ],
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note.html")
        self.assertEqual(response.context["note"], self.test_note)

    # def test_expired_note_response(self):
    #     self.test_note.creation_date =  timezone.now() - datetime.timedelta(days=6, hours=1)
    #     print(self.test_note.creation_date)
    #     self.test_note.view_count = 20
    #     url = reverse("note", args=[self.test_note.id,])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "notes/note.html")
    #     print("note is",response.context['note'])

    def test_wrong_code_response(self):
        self.test_note.view_count = 20
        url = reverse(
            "note",
            args=[
                self.test_note.id,
            ],
        )
        Note.delete(self.test_note)
        response = self.client.get(url)
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 404)
