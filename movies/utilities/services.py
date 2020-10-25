
import random
from typing import Iterable

from movies.adapters.repository import  AbstractRepository
from movies.domain.model import Movie, Genre


def get_genre_names(repo: AbstractRepository):
    genres = repo.get_genres()
    genre_names = [genre.genre_name for genre in genres]

    return genre_names


def get_random_movies(quantity, repo: AbstractRepository):
    movie_count = repo.get_number_of_movies()

    if quantity > movie_count:
        quantity = movie_count - 1

    random_ranks = random.sample(range(1, movie_count), quantity)
    movies = repo.get_movies_by_rank(random_ranks)

    return movies_to_dict(movies)


def movies_on_page(current_rank, repo: AbstractRepository):
    movie_list = [current_rank, current_rank + 1, current_rank + 2]

    movies = repo.get_movies_by_rank(movie_list)

    return movies_to_dict(movies)

# ============================================
# Functions to convert dicts to model entities
# ============================================


def movie_to_dict(movie: Movie):
    movie_dict = {
        'rank': movie.rank,
        'title': movie.title,
        'genres': genres_to_str(movie.genres),
        'plot': movie.description
    }
    return movie_dict


def movies_to_dict(movies: Iterable[Movie]):
    return [movie_to_dict(movie) for movie in movies]


def genres_to_str(list_of_genres: Iterable[Genre]):
    string = ''

    for genre in list_of_genres:
        string += genre.genre_name + ', '

    return string[:-2]
