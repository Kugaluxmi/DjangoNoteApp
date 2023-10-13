from django import forms
from django.core.exceptions import ValidationError
from .models import Notes

class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        labels = {
            'text' : 'Your Notes here : '
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError("We Only accept notes about Django! ")
        return title