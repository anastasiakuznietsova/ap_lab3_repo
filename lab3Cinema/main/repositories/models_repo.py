from .base_repo import BaseRepo
from main.models import Movie,Showtime,Ticket,MovieSession,Viewer
from main.forms import TicketForm, MovieSessionForm

class ViewerRepo(BaseRepo):
    def __init__(self):
        super().__init__(Viewer)

class MovieRepo(BaseRepo):
    def __init__(self):
        super().__init__(Movie)

    def getByTitle(self, title):
        obj=self.model.objects.get(title=title)
        return obj.id

class ShowtimeRepo:
    def get_showtime_by_movie_title(self, title=''):
        return Showtime.objects.filter(movie__title__icontains=title)
    def get_all_movie_names(self):
        return Movie.objects.all()

class TicketMovieSessionRepo(BaseRepo):
    def __init__(self):
        super().__init__(Ticket)
        super().__init__(MovieSession)

    def bookingTicket(self,ticket_data, session_data,viewer):
        ticket_form = TicketForm(ticket_data)
        session_form = MovieSessionForm(session_data)
        if ticket_form.is_valid() and session_form.is_valid():
            ticket = ticket_form.save(commit=False)
            session = session_form.save(commit=False)
            ticket.viewer=viewer
            ticket.save()
            session.ticket = ticket
            session.save()
            return ticket, session
        return None, None

    def updateTicket(self, ticket_id, ticket_data, session_data):
        ticket = Ticket.objects.get(id=ticket_id)
        session = MovieSession.objects.get(id=ticket_id)

        ticket_form = TicketForm(ticket_data, instance=ticket)
        session_form = MovieSessionForm(session_data, instance=session)

        if ticket_form.is_valid() and session_form.is_valid():
            ticket = ticket_form.save()
            session = session_form.save()
            return ticket, session
        return None, None

    def getTicketWithSession(self, viewer):
        tickets = Ticket.objects.filter(viewer=viewer)
        movie_sessions = MovieSession.objects.filter(ticket__in=tickets)

        ticket_movie_info = []
        for ticket in tickets:
            movie_session = movie_sessions.filter(ticket=ticket).first()
            if movie_session:
                ticket_movie_info.append({
                    'ticket': ticket,
                    'movie_session': movie_session,
                })
        return ticket_movie_info