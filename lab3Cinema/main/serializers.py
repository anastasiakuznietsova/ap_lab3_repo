from .models import Viewer, Ticket, MovieSession, Showtime
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'password',]
class ViewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viewer
        fields = [
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'birth_date'
        ]

class TicketSerializer(serializers.ModelSerializer):
    viewer= serializers.PrimaryKeyRelatedField(many=False,queryset=Viewer.objects.all())
    showtime = serializers.PrimaryKeyRelatedField(many=False,queryset=Showtime.objects.all())
    class Meta:
        model = Ticket
        fields = ['showtime',
                  'viewer']

class ShowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Showtime
        fields=['show_date',
                'price']

class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = '__all__'