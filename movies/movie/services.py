from typing import List, Iterable
from movies.adapters.repository import AbstractRepository
from movies.domain.model import Movie, Genre, Actor, Director


class NonExistentMovieException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def get_movie(movie_rank: int, repo: AbstractRepository):
    movie = repo.get_movie(movie_rank)

    if movie is None:
        raise NonExistentMovieException

    return movie_to_dict(movie)


def get_first_movie(repo: AbstractRepository):
    movie = repo.get_first_movie()

    return movie_to_dict(movie)


def get_last_movie(repo: AbstractRepository):
    movie = repo.get_last_movie()

    return movie_to_dict(movie)


def get_movie_by_a_rank(rank, repo: AbstractRepository):
    movie = repo.get_movie(rank)
    movie_dict = movie_to_dict(movie)
    prev_rank = next_rank = None
    if movie.rank == 1:
        prev_rank = None
        next_rank = 4
    elif movie.rank == 1000:
        prev_rank = 997
        next_rank = None
    elif 1 < movie.rank < 1000:
        prev_rank = movie.rank - 3
        next_rank = movie.rank + 3

    return movie_dict, prev_rank, next_rank


def get_movies_by_rank(rank_list, repo: AbstractRepository):
    movies = repo.get_movies_by_rank(rank_list)
    movies_as_dict = movies_to_dict(movies)

    return movies_as_dict


def mov_on_page(current_rank, repo: AbstractRepository):
    rank_list = [current_rank, current_rank + 1, current_rank + 2]
    movies = get_movies_by_rank(rank_list, repo)

    return movies


def get_movies_ranks_for_genre(genre_name, repo: AbstractRepository):
    movie_ranks = repo.get_movie_ranks_for_genre(genre_name)

    return movie_ranks

# ============================================
# Functions to convert model entities to dicts
# ============================================


def movie_to_dict(movie: Movie):
    movie_dict = {
        'rank': movie.rank,
        'title': movie.title,
        'director': movie.director,
        'year': movie.release_year,
        'plot': movie.description,
        'runtime': movie.runtime_minutes,
        'genres': genres_to_dict(movie.genres),
        'actors': actors_to_dict(movie.actors),
        'actors_str': actors_to_str(movie.actors),
        'genres_str': genres_to_str(movie.genres),
        'rating': movie.rating,
        'revenue': movie.revenue,
        'metascore': movie.metascore,
        'votes': movie.votes
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def genre_to_dict(genre: Genre):
    genre_dict = {
        'name': genre.genre_name,
        'tagged_movies': [movie.rank for movie in genre.tagged_movies]
    }
    return genre_dict


def genres_to_dict(genres: Iterable[Genre]):
    return [genre_to_dict(genre) for genre in genres]


def actor_to_dict(actor: Actor):
    actor_dict = {
        'name': actor.actor_name
    }
    return actor_dict


def actors_to_dict(actors: Iterable[Actor]):
    return [actor_to_dict(actor) for actor in actors]


def actors_to_str(list_of_actors: Iterable[Actor]):
    return '{}, {}, {}, {}'.format(list_of_actors[0].actor_name,
                                   list_of_actors[1].actor_name,
                                   list_of_actors[2].actor_name,
                                   list_of_actors[3].actor_name)


def genres_to_str(list_of_genres: Iterable[Genre]):
    string = ''

    for genre in list_of_genres:
        string += genre.genre_name + ', '

    return string[:-2]
