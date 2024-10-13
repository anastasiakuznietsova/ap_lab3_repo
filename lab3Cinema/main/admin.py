from django.contrib import admin
from .models import MovieGenre,AgeRestrictions,AnimationFormat,Movie,Room,Seat,Showtime,Viewer,Ticket,MovieSession
# Register your models here.

admin.site.register(MovieGenre)
admin.site.register(AgeRestrictions)
admin.site.register(AnimationFormat)
admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(Showtime)
admin.site.register(Viewer)
admin.site.register(Ticket)
admin.site.register(MovieSession)