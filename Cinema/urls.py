from django.db import router
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from movie import views
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'usersAPI', views.UserViewSet)
router.register(r'movieAPI', views.MovieViewSet)
router.register(r'movieRoomAPI', views.MovieRoomViewSet)
router.register(r'sessionAPI', views.SessionViewSet)
router.register(r'movieListApi', views.MovieViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),  # Админ урл
    path('', include('authorization.urls')),  # Инклюд(Ссылка на) урлы Авторизации
    path('', include('movie.urls_movie')),  # Инклюд(Ссылка на) урлы Фильмов и пр.
    path('', include(router.urls)),  # Инклюд на Роутеры
    path('api-auth/', include('rest_framework.urls')),  # инклюд на рест фреймворк
]
# Настройка для расдачи медиа файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
