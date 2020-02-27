from rest_framework import serializers
from movie.models import Movie, MovieRoom, Session, Ticket
from authorization.models import User


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['name', 'description', 'category', 'poster', 'year', 'url', 'youtube']


class MovieRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRoom
        fields = ['room_name', 'room_size']
