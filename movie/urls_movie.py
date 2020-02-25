from django.urls import path
from .views import *
from authorization.views import UserPage

urlpatterns = [
    path('create_session/', CreateSession.as_view(), name='create_session'),
    path('profile/', UserPage, name='profile'),
    path('create/', MovieCreate.as_view(), name='create'),
    path('', MovieView.as_view(), name='home'),
    path('<slug:slug>/', MovieDetail.as_view(), name='movieinfo'),
    path('CreateReview/', MovieReviewCreate.as_view(), name='movieReview'),
]
