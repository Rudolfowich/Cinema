from django.urls import path
from .views import *
from authorization.views import UserPage

urlpatterns = [
    path('create_session/', CreateSession.as_view(), name='create_session'),
    path('profile/', UserPage, name='profile'),
    path('create/', MovieCreate.as_view(), name='create'),
    path('', MovieView.as_view(), name='home'),
    path('Purchases/', PurchasesListView.as_view(), name='purchases'),
    path('buy_ticket/', BuyTicket.as_view(), name='buy_ticket'),
    path('CreateRoom/', MovieRoomCreate.as_view(), name='MovieRoomCreate'),
    path('SessionList/', SessionList.as_view(), name='sessialister'),
    path('SessionDeleteList/', ListDeleteSession.as_view(), name='session_list_delete'),
    path('CreateReview/', MovieReviewCreate.as_view(), name='movieReview'),
    path('filter/', FilterSessionView.as_view(), name='filter'),
    path('update_session/<int:pk>/', UpdateSession.as_view(), name='update'),
    path('<int:pk>/delete_session/', DeleteSession.as_view(), name='delete_session'),
    path('<slug:slug>/', MovieDetail.as_view(), name='movieinfo'),
]
