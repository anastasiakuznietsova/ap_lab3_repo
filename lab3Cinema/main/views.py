from django.contrib.auth.models import User

from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import MovieSerializer,UserSerializer, ViewerSerializer, TicketSerializer, ShowtimeSerializer, MovieSessionSerializer
from rest_framework import status

from .models import Viewer, Ticket, MovieSession, Showtime, Movie


class ViewerViewSet(viewsets.ModelViewSet):
    queryset = Viewer.objects.all()
    serializer_class = ViewerSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class ShowtimeViewSet(viewsets.ModelViewSet):
    queryset = Showtime.objects.all()
    serializer_class=ShowtimeSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer

class UserList(APIView):
    def get(self, request, format=None):
        if request.user.is_authenticated:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def post(self, request, format=None):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            validated_data = user_serializer.validated_data
            user = User(username=validated_data['username'])
            password = validated_data.get("password")
            if password:
                user.set_password(password)
            user.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserDetail(APIView):
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404
    def get_viewer(self, username):
        try:
            return Viewer.objects.get(phone_number=username)
        except Viewer.DoesNotExist:
            raise Http404
    def get_ticket(self, viewer_id):
        try:
            return Ticket.objects.filter(viewer=viewer_id)
        except Ticket.DoesNotExist:
            raise Http404
    def get(self, request):
        if request.user.is_authenticated:
            user = self.get_user(request.user.username)
            viewer = self.get_viewer(request.user.username)
            ticket=self.get_ticket(viewer.id)
            user_serializer = UserSerializer(user)
            viewer_serializer = ViewerSerializer(viewer)
            ticket_serializer = TicketSerializer(ticket,many=True)
            return Response({'user':user_serializer.data,
                             'viewer':viewer_serializer.data,
                             'ticket':ticket_serializer.data})
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    def put(self, request, format=None):
        if request.user.is_authenticated:
            user = self.get_user(request.user.username)
            user_serializer = UserSerializer(user,data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    def delete(self, request, format=None):
        if request.user.is_authenticated:
            user = self.get_user(request.user.username)
            viewer = self.get_viewer(request.user.username)
            user.delete()
            viewer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

class ViewerList(APIView):
    def get(self, request, format=None):
        viewers = Viewer.objects.all()
        serializer = ViewerSerializer(viewers, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ViewerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ViewerDetail(APIView):
    def get_object(self, pk):
        try:
            return Viewer.objects.get(pk=pk)
        except Viewer.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        viewer = self.get_object(pk)
        serializer = ViewerSerializer(viewer)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        viewer = self.get_object(pk)
        serializer = ViewerSerializer(viewer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        viewer=self.get_object(pk)
        viewer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TicketList(APIView):
    def get(self, request, format=None):
        if request.user.is_superuser:
            tickets=Ticket.objects.all()
            serializer = TicketSerializer(tickets, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_403_FORBIDDEN)
    def post(self, request, format=None):
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class TicketDetail(APIView):
    def get_session(self,pk):
        try:
            return MovieSession.objects.get(pk=pk)
        except MovieSession.DoesNotExist:
            raise Http404
    def get_ticket(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        session=self.get_session(pk)
        ticket=self.get_ticket(session.ticket)
        session_serializer = MovieSessionSerializer(session)
        ticket_serializer = TicketSerializer(ticket)
        return Response({"session":session_serializer,
                         "ticket":ticket_serializer})
    def put (self, request, pk, format=None):
        session = self.get_session(pk)
        ticket = self.get_ticket(session.ticket)
        serializer = TicketSerializer(ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        session = self.get_session(pk)
        ticket = self.get_ticket(session.ticket)
        ticket.delete()
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ShowtimeList(APIView):
    def get(self, request):
        showtime = Showtime.objects.all()
        serializer = ShowtimeSerializer(showtime, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        if request.user.is_superuser:
            serializer = ShowtimeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
class ShowtimeDetails(APIView):
    def get_object(self, pk):
        try:
            return Showtime.objects.get(pk=pk)
        except Showtime.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        showtime_movie = self.get_object(pk)
        serializer = ShowtimeSerializer(showtime_movie)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        if request.user.is_superuser:
            showtime_movie = self.get_object(pk)
            serializer = ShowtimeSerializer(showtime_movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
    def delete(self, request, pk):
        if request.user.is_superuser:
            showtime_movie=self.get_object(pk)
            showtime_movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

class MovieList(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        if request.user.is_superuser:
            serializer = MovieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
class MovieDetails(APIView):
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        movie = self.get_object(pk)
        serializer = ShowtimeSerializer(movie)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        if request.user.is_superuser:
            movie = self.get_object(pk)
            serializer = ShowtimeSerializer(movie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)
    def delete(self, request, pk):
        if request.user.is_superuser:
            movie=self.get_object(pk)
            movie.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)