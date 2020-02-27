from django.urls import path
from authorization import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),  # Урл на логин
    path('logout/', views.LogoutView.as_view(), name='logout'),  # Урл на логаут
    path('register/', views.RegisterCreateView.as_view(), name='register'),  # Урл на Регистрацию
]