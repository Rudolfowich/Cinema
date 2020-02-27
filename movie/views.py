from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from .models import Movie, Session, Images, MovieRoom, Ticket
from .forms import MovieForm, SessionForm, ImageReview, MovieSizeForm, TicketForm


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


class MovieDetail(DetailView):
    # Подробно о фильме #
    model = Movie
    slug_field = "url"
    template_name = 'movie/movie_info.html'


class MoviePhoto(DetailView):
    model = Images


class MovieReviewCreate(CreateView, LoginRequiredMixin):
    model = Images
    form_class = ImageReview
    template_name = 'movie/createReview.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated) or (not request.user.is_superuser):
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class MovieRoomCreate(CreateView, LoginRequiredMixin):
    model = MovieRoom
    form_class = MovieSizeForm
    template_name = 'movie/create_room.html'
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated) or (not request.user.is_superuser):
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)


class SessionList(ListView):
    model = Session
    template_name = 'movie/session_list.html'


class GenreYear:

    def get_category(self):
        return Movie.objects.values("category")

    def get_years(self):
        return Movie.objects.values("year")


class MovieView(GenreYear, ListView):
    model = Movie
    queryset = Movie.objects.all()
    template_name = 'movie/afisha.html'


class FilterSessionView(GenreYear, ListView):
    def get_queryset(self):
        queryset = Movie.objects.filter(category__in=self.request.GET.getlist("category"),
                                        year__in=self.request.GET.getlist("year"))
        return queryset


class BuyTicket(CreateView, LoginRequiredMixin):
    model = Ticket
    form_class = TicketForm
    http_method_names = ['post', 'get']
    template_name = 'movie/buy_ticket.html'
    session = None
    success_url = '/'

    def form_valid(self, form):
        obj = form.save(commit=False)
        session_form = form.data['session']
        movie_session = Session.objects.get(id=session_form)
        quantity = int(form.data['quantity'])
        cost = movie_session.price * quantity
        show_purchases = int(self.request.user.sum_all)
        if int(self.request.user.money) < int(cost):
            return HttpResponse('Не хватает бабулетов')
        else:
            self.request.user.money -= cost
            self.request.user.sum_all += cost
            self.request.user.save()
        obj.user = self.request.user
        obj.session = movie_session
        movie_room = movie_session.room_name
        movie_room.room_size -= quantity
        if int(movie_room.room_size <= -1):
            return HttpResponse('Увы закончились места')
        movie_room.save()
        obj.save()
        return HttpResponseRedirect('/')


class PurchasesListView(ListView):
    model = Ticket
    context_object_name = 'tickets'
    template_name = 'movie/purchases.html'

    def get_queryset(self):
        return Ticket.objects.filter(user=self.request.user)


class ListDeleteSession(ListView):
    model = Session
    template_name = 'movie/DeleteSession.html'


class DeleteSession(DeleteView):
    model = Session
    template_name = 'movie/DeleteSession.html'

    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated) or (not request.user.is_superuser):
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     context = self.get_context_data(object=self.object)
    #     if self.object.movie_room.size < self.object.places:
    #         return HttpResponse('Unable to change')
    #             """Нужно тестировать"""


class UpdateSession(UpdateView):
    model = Session
    form_class = SessionForm
    template_name = 'movie/session_update.html'
    success_url = reverse_lazy('sessialister')

    def dispatch(self, request, *args, **kwargs):
        if (not request.user.is_authenticated) or (not request.user.is_superuser):
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)

    # def form_valid(self, form):
    #     places = int(form.data['places'])
    #     comparison_room = int(form.data['movie_room'])
    #     next_comparion = Session.objects.get(movie_room=places)
    #     if next_comparion.movie_room.size < places:
    #         raise PermissionDenied()
    #         """Нужно тестировать"""
