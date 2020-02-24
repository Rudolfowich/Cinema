from django.forms import ModelForm
from django import forms
from movie.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'category', 'poster', 'year', 'url']
