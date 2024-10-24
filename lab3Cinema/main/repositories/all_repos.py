from .models_repo import MovieRepo,ShowtimeRepo,TicketMovieSessionRepo,MovieRepo

class allRepos:
    def __init__(self):
        self.movies=MovieRepo()
        self.showtimes=ShowtimeRepo()
        self.movie_sessions_tickets = TicketMovieSessionRepo()