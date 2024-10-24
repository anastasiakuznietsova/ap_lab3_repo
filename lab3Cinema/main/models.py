from django.db import models

class MovieGenre(models.Model):
    genre_name = models.CharField(max_length=20)
    def __str__(self):
        return self.genre_name
    class Meta:
        db_table = 'MovieGenre'


class AgeRestrictions(models.Model):
    restriction = models.CharField(max_length=10)
    def __str__(self):
        return self.restriction
    class Meta:
        db_table = 'AgeRestrictions'


class AnimationFormat(models.Model):
    anima_format = models.CharField(max_length=2)
    def __str__(self):
        return self.anima_format
    class Meta:
        db_table = 'AnimationFormat'


class Movie(models.Model):
    title = models.CharField(max_length=50,null=False)
    mov_length = models.IntegerField()
    premiere = models.DateField()
    mvdescription = models.CharField(max_length=100)
    moviegenre = models.ForeignKey('MovieGenre', on_delete=models.CASCADE)
    agerestrictions = models.ForeignKey('AgeRestrictions', on_delete=models.CASCADE)
    animationformat = models.ForeignKey('AnimationFormat', on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'Movie'


class Room(models.Model):
    room_number=models.IntegerField(null=False)
    def __str__(self):
        return str(self.room_number)
    class Meta:
        db_table = 'Room'

class Seat(models.Model):
    seat_num=models.IntegerField(null=False)
    isAvailable=models.BooleanField()
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    def __str__(self):
        return f'Room: {self.room}   Seat: {self.seat_num}'
    class Meta:
        db_table = 'Seat'


class Showtime(models.Model):
    show_date=models.DateField()
    price=models.DecimalField(max_digits=4,decimal_places=2)
    movie=models.ForeignKey('Movie', on_delete=models.CASCADE)
    room=models.ForeignKey('Room', on_delete=models.CASCADE)
    startsAt=models.TimeField()
    endsAt=models.TimeField()
    def __str__(self):
        return f'{self.movie}     {self.show_date}'
    def getTimeline(self):
        return f'{self.startsAt} -- {self.endsAt}'
    class Meta:
        db_table = 'Showtime'


class Viewer(models.Model):
    first_name=models.CharField(max_length=20,null=False)
    last_name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=15,null=False)
    birth_date=models.DateField()
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    class Meta:
        db_table = 'Viewer'


class Ticket(models.Model):
    showtime=models.ForeignKey('Showtime', on_delete=models.CASCADE)
    viewer=models.ForeignKey('Viewer', on_delete=models.CASCADE)
    def __str__(self):
        return f'Showtime: {self.showtime} | Viewer: {self.viewer}'
    class Meta:
        db_table = 'Ticket'


class MovieSession(models.Model):
    seat=models.ForeignKey('Seat', on_delete=models.CASCADE)
    ticket=models.ForeignKey('Ticket', on_delete=models.CASCADE)
    def __str__(self):
        return f'Ticket: {self.ticket} | Seat: {self.seat}'
    class Meta:
        db_table = 'MovieSession'