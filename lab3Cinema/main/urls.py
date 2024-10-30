from django.urls import path,include
from main import views

# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register(r'viewer',views.ViewerViewSet,basename='viewer')
# router.register(r'ticket',views.TicketViewSet,basename='ticket')
# router.register(r'user',views.UserViewSet,basename='user')
app_name = 'main'
urlpatterns = [
    # path('',include(router.urls)),
    path('viewers/',views.ViewerList.as_view()),
    path('viewers/<int:pk>/',views.ViewerDetail.as_view()),
    path('users/',views.UserList.as_view()),
    path('users/info/',views.UserDetail.as_view()),
    path('showtime/',views.ShowtimeList.as_view(), name='showtime'),
    #path('showtime/<int:pk>/',views.ShowtimeDetails.as_view(), name = 'showtime-details'),
    path('movies/',views.MovieList.as_view(),name='movies'),
    path('showtime/<int:pk>/',views.MovieDetails.as_view(), name='movie-details'),
    path('showtime/create-showtime/',views.ShowtimeCreate.as_view(), name='create-showtime'),
    path('showtime/create-movie/',views.MovieCreate.as_view(), name='create-movie'),
    path('showtime/delete-showtime/<int:pk>',views.ShowtimeDelete.as_view(), name='delete-show'),
    path('showtime/<int:pk>/update-movie/',views.MovieUpdate.as_view(), name='update-movie'),
    path('showtime/<int:pk>/delete-movie/',views.MovieDelete.as_view(), name='delete-movie'),
    path('tickets/',views.TicketList.as_view()),
    path('tickets/<int:pk>/',views.TicketDetail.as_view()),


    path('list-objects/', views.itemList, name='list-objects'),
    path('list-objects/delete/<int:id>/', views.deleteItem, name='delete-object'),

]