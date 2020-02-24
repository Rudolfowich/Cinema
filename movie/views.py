from urllib import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, DetailView
from django.views.generic.base import View
from .models import Movie, Session, Images
from .forms import MovieForm


class MovieView(ListView):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, "movie/afisha.html", {"movie_list": movies})


class MovieCreate(CreateView, LoginRequiredMixin):
    model = Movie
    template_name = "movie/create.html"
    form_class = MovieForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated) or (not request.user.is_superuser):
                return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class CreateSession(CreateView, LoginRequiredMixin):
    model = Session
    template_name = 'movie/create_session.html'
    http_method_names = ['post', 'get']
    success_url = '/'


class MovieDetail(ListView):
    # Подробно о фильме #
    def get(self, request, slug, *args, **kwargs):
        movie = Movie.objects.get(url=slug)
        return render(request, "movie/movie_info.html", {"movie": movie})


class MoviePhoto(DetailView):
    model = Images
    slug_field = "url"



