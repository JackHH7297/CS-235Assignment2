import pytest

from movies.movie import services as movies_services
from movies.movie.services import NonExistentMovieException


def test_can_get_movie(in_memory_repo):
    movie_rank = 1

    movie_as_dict = movies_services.get_movie(movie_rank, in_memory_repo)

    assert movie_as_dict['rank'] == 1
    assert movie_as_dict['title'] == 'Guardians of the Galaxy'

    genre_names = [dict1['name'] for dict1 in movie_as_dict['genres']]
    assert 'Action' in genre_names
    assert 'Adventure' in genre_names
    assert 'Sci-Fi' in genre_names

    actor_names = [dict2['name'] for dict2 in movie_as_dict['actors']]
    assert 'Chris Pratt' in actor_names
    assert 'Vin Diesel' in actor_names
    assert 'Zoe Saldana' in actor_names
    assert 'Bradley Cooper' in actor_names
    assert 'Leonardo DiCaprio' not in actor_names


def test_cannot_get_movie_with_non_existent_rank(in_memory_repo):
    movie_rank = 1001

    # Call the service layer to attempt to retrieve the movie with rank 1001
    with pytest.raises(movies_services.NonExistentMovieException):
        movies_services.get_movie(movie_rank, in_memory_repo)


def test_get_first_movie(in_memory_repo):
    movie_as_dict = movies_services.get_first_movie(in_memory_repo)

    assert movie_as_dict['rank'] == 1
    assert movie_as_dict['title'] == 'Guardians of the Galaxy'


def test_get_last_movie(in_memory_repo):
    movie_as_dict = movies_services.get_last_movie(in_memory_repo)

    assert movie_as_dict['rank'] == 1000
    assert movie_as_dict['title'] == 'Nine Lives'


def test_get_movie_by_rank_with_one_rank(in_memory_repo):
    target_rank = 555
    movie_as_dict, prev_rank, next_rank = movies_services.get_movie_by_a_rank(target_rank, in_memory_repo)

    assert movie_as_dict['rank'] == 555
    assert prev_rank == 552
    assert next_rank == 558


# Check retrieval of movies with a list of ranks
def test_get_movies_by_ranks(in_memory_repo):
    list_of_ranks = [1, 2, 1000, 1001, 2000]
    movies_as_dict = movies_services.get_movies_by_rank(list_of_ranks, in_memory_repo)

    # Check that 3 valid movies were returned from the query.
    assert len(movies_as_dict) == 3

    # Check that the movie ranks returned were 1, 2 and 1000.
    movie_ids = [movie['rank'] for movie in movies_as_dict]
    assert set([1, 2, 1000]).issubset(movie_ids)




