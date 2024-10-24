from django.urls import path,include
from . import views

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'viewer',views.ViewerViewSet,basename='viewer')
# router.register(r'ticket',views.TicketViewSet,basename='ticket')
# router.register(r'user',views.UserViewSet,basename='user')

urlpatterns = [
    # path('',include(router.urls)),
    path('viewers/',views.ViewerList.as_view()),
    path('viewers/<int:pk>/',views.ViewerDetail.as_view()),
    path('users/',views.UserList.as_view()),
    path('users/info/',views.UserDetail.as_view()),
    path('showtime/',views.ShowtimeList.as_view()),
    path('showtime/<int:pk>/',views.ShowtimeDetails.as_view()),
    path('movies/',views.MovieList.as_view()),
    path('movies/<int:pk>/',views.MovieDetails.as_view()),
    path('tickets/',views.TicketList.as_view()),
    path('tickets/<int:pk>/',views.TicketDetail.as_view()),

]