from urllib import request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, DetailView
from django.views.generic.base import View
from .models import Movie, Session, Images, MovieRoom
from .forms import MovieForm, SessionForm, ImageReview, MovieSizeForm


class MovieView(ListView):
    paginate_by = 3

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
    form_class = SessionForm
    http_method_names = ['post', 'get']
    success_url = '/'
    login_url = '/login'

    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated) or (not request.user.is_superuser):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class MovieDetail(ListView):
    # Подробно о фильме #
    def get(self, request, slug, *args, **kwargs):
        movie = Movie.objects.get(url=slug)
        return render(request, "movie/movie_info.html", {"movie": movie})


class MoviePhoto(DetailView):
    model = Images
    slug_field = "url"


class MovieReviewCreate(CreateView, LoginRequiredMixin):
    model = Images
    form_class = ImageReview
    template_name = 'movie/createReview.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated) or (not request.user.is_superuser):
            raise PermissionDenied("Не лезь блядь!")
        return super().dispatch(request, *args, **kwargs)


class MovieRoomCreate(CreateView, LoginRequiredMixin):
    model = MovieRoom
    form_class = MovieSizeForm
    template_name = 'movie/create_room.html'
    success_url = '/'


class DateMoney:
    def get_price(self):
        return Session.objects.values('price')

    def get_date(self):
        return Session.objects.values('start')


class SessionList(DateMoney, ListView):
    model = Session
    template_name = 'movie/session_list.html'
