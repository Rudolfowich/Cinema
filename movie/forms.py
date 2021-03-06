from django import forms
from django.forms import ModelForm, DateInput, DateTimeInput, MultiWidget

from movie.models import Movie, Session, Images, MovieRoom, Ticket


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'category', 'poster', 'year', 'url', 'youtube']


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = (
            'movie',
            'room_name',
            'start',
            'end',
            'price',
            'places',
        )
        widgets = {
            'start': DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
            'end': DateInput(format='%d/%m/%Y', attrs={
                'class': 'form-control', 'placeholder': 'Select a date', 'type': 'date'}),
        }


class ImageReview(ModelForm):
    class Meta:
        model = Images
        fields = 'image', 'movie'


class MovieSizeForm(ModelForm):
    class Meta:
        model = MovieRoom
        fields = 'room_name', 'room_size'


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = (
            'quantity', 'session')
