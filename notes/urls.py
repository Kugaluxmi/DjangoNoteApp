from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NoteListView.as_view(), name="notes.list"),
    path('note/<int:pk>', views.NotesDetailView.as_view(), name="note.detail"),
    path('note/<int:pk>/edit', views.NotesUpdateView.as_view(), name="note.update"),
    path('note/<int:pk>/delete', views.NotesDeleteView.as_view(), name="note.delete"),
    path('note/new', views.NotesCreateView.as_view(), name="note.new"),
]