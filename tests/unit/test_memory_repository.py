import os
from typing import List

import pytest

from movies.domain.model import Movie, Director, Genre, Actor, User, Review, make_review
from movies.adapters import memory_repository
from movies.adapters.memory_repository import MemoryRepository
from movies.adapters.repository import RepositoryException

data_path = os.path.join('C:', os.sep, 'Users', 'Jack', 'Documents', 'CS-235',
                                  'Assignment2',
                                  'tests', 'data', "Data1000Movies.csv")


@pytest.fixture
def in_memory_repo():
    repo = MemoryRepository()
    memory_repository.populate(data_path, repo)
    return repo


def test_repository_can_add_a_user(in_memory_repo):
    user = User('Jack', '111241')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('Jack') is user


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None


def test_repository_can_retrieve_movie_count(in_memory_repo):
    number_of_movies = in_memory_repo.get_number_of_movies()
    assert number_of_movies == 1000


def test_repository_can_add_movie(in_memory_repo):
    movie = Movie("Your name", 2016)
    in_memory_repo.add_movie(movie)

    assert in_memory_repo.get_movie(1001) is movie


def test_repository_can_retrieve_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(1)

    assert movie.title == "Guardians of the Galaxy"
    assert movie.genres == [Genre("Action"), Genre("Adventure"), Genre("Sci-Fi")]
    assert movie.runtime_minutes == 121
    assert movie.is_tagged_by(Genre("Action"))
    assert movie.director.director_full_name == 'James Gunn'
    assert movie.has_actor('Chris Pratt')


def test_repository_does_not_retrieve_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(1001)
    assert movie is None


def test_repository_can_get_first_movie(in_memory_repo):
    movie = in_memory_repo.get_first_movie()
    assert movie.title == "Guardians of the Galaxy"


def test_repository_can_get_last_movie(in_memory_repo):
    movie = in_memory_repo.get_last_movie()
    assert movie.title == "Nine Lives"


def test_repository_can_get_articles_by_ids(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rank([1, 1000, 2])
    assert len(movies) == 3
    assert movies[0].title == "Guardians of the Galaxy"
    assert movies[1].title == "Nine Lives"
    assert movies[2].title == "Prometheus"


def test_repository_does_not_retrieve_movie_for_non_existent_rank(in_memory_repo):
    movie = in_memory_repo.get_movies_by_rank([2, 1001])
    assert len(movie) == 1
    assert movie[0].title == "Prometheus"


def test_repository_returns_an_empty_list_for_non_existent_ids(in_memory_repo):
    movies = in_memory_repo.get_movies_by_rank([0, 120000])

    assert len(movies) == 0


def test_repository_can_add_a_genre(in_memory_repo):
    genre = Genre('Action')
    in_memory_repo.add_genre(genre)

    assert genre in in_memory_repo.get_genres()


def test_repository_can_retrieve_genres(in_memory_repo):
    genres: List[Genre] = in_memory_repo.get_genres()

    print(genres)


