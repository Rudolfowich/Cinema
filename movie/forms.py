from django.forms import ModelForm, DateInput, TimeInput, DateTimeInput
from django import forms
from movie.models import Movie,Session


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'category', 'poster', 'year', 'url', 'youtube']


class SessionForm(ModelForm):
    class Meta:
        model = Session
        fields = (
            'name',
            'room_name',
            'start',
            'end',
            'price',
        )
