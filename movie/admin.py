from django.contrib import admin
from .models import Session, MovieRoom, Movie, Images
from authorization.models import User
admin.site.register(Session)
admin.site.register(MovieRoom)

admin.site.register(User)
admin.site.register(Images)
admin.site.register(Movie)
