from django.urls import path
from main import views
from .views import (showtime, movie_information, viewer_information,
                    ticketCancellation,bookATicket,updateTicket,JSONresponse)
from .views import loginPage,logoutPage,registerPage

urlpatterns = [
    path('login/',loginPage,name='login'),
    path('logout/',logoutPage,name='logout'),
    path('register/',registerPage,name='register'),
    path('', showtime, name='showtime' ),
    path('booking/', bookATicket, name='booking' ),
    path('movie-information/<str:title>/',movie_information, name='movie-information'),
    path('accounts-info/', viewer_information, name='accounts-information'),
    path('update-ticket/<int:id>', updateTicket, name='update-ticket'),
    path('cancel-ticket/<int:id>', ticketCancellation, name='cancel-ticket'),
    path('json-response/', JSONresponse, name='json-response'),
]