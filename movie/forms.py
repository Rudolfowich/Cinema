from django.forms import ModelForm, DateInput, TimeInput, DateTimeInput
from django import forms
from movie.models import Movie, Session, Images


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


class ImageReview(MovieForm):
    class Meta:
        model = Images
        fields = 'image', 'movie'
