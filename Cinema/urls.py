from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ урл
    path('', include('authorization.urls')),  # Инклюд(Ссылка на) урлы Авторизации
    path('', include('movie.urls_movie')),  # Инклюд(Ссылка на) урлы Фильмов и пр.
]
# Настройка для расдачи медиа файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
