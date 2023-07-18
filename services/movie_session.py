from db.models import MovieSession
import datetime


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int
) -> MovieSession:
    movie_session = MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall_id=cinema_hall_id,
        movie_id=movie_id
    )

    return movie_session


def get_movies_sessions(session_date: str = None) -> MovieSession:
    sessions = MovieSession.objects.all()
    if session_date:
        sessions = sessions.filter(show_time__date=session_date)
    return sessions


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
    session_id: int,
    show_time: datetime = None,
    movie_id: int = None,
    cinema_hall_id: int = None,
) -> MovieSession:
    updated = MovieSession.objects.get(id=session_id)
    if show_time:
        updated.show_time = show_time
    if movie_id:
        updated.movie_id = movie_id
    if cinema_hall_id:
        updated.cinema_hall_id = cinema_hall_id

    updated.save()

    return updated


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()