import csv
import os
from typing import List

from movies.domain.model import Director, Actor, Movie, Genre, User, Review, make_review, make_genre_association
from movies.adapters.repository import AbstractRepository
from bisect import bisect, bisect_left, insort_left
from movies.adapters.movie_file_csv_reader import MovieFileCSVReader


class MemoryRepository(AbstractRepository):

    def __init__(self):
        self._movies = list()
        self._movies_rank = dict()
        self._genres = list()
        self._users = list()
        self._actors = list()
        self._directors = list()
        self._reviews = list()

    def add_user(self, user: User):
        self._users.append(user)

    def get_user(self, username) -> User:
        return next((user for user in self._users if user.user_name == username.lower()), None)

    def add_movie(self, movie: Movie):
        if movie.rank is None:
            movie.rank = len(self._movies) + 1
        self._movies.append(movie)
        self._movies_rank[movie.rank] = movie

    def get_movie(self, rank: int) -> Movie:
        movie = None

        try:
            movie = self._movies_rank[rank]
        except KeyError:
            pass
        return movie

    def get_movie_rank_by_name(self, name: str):
        movie = None

        for items in self._movies:
            if items.title == name:
                return items.rank

    def get_number_of_movies(self):
        return len(self._movies)

    def get_first_movie(self):
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[0]
        return movie

    def get_last_movie(self):
        movie = None

        if len(self._movies) > 0:
            movie = self._movies[-1]
        return movie

    def get_movies_by_rank(self, rank_list):
        existing_ranks = [rank for rank in rank_list if rank in self._movies_rank]

        movies = [self._movies_rank[rank] for rank in existing_ranks]
        return movies

    def get_movie_ranks_for_genre(self, genre_name: str):
        genre = next((genre for genre in self._genres if genre.genre_name == genre_name), None)

        if genre is not None:
            movie_ranks = [movie.rank for movie in genre.tagged_movies]
        else:
            movie_ranks = list()

        return movie_ranks

    def add_genre(self, genre: Genre):
        self._genres.append(genre)

    def get_genres(self) -> List[Genre]:
        print("In memory repo, getting genres!")
        return self._genres

    def add_actor(self, actor: Actor):
        self._actors.append(actor)

    def get_actors(self) -> List[Actor]:
        return self._actors

    def add_director(self, director: Director):
        self._directors.append(director)

    def get_directors(self) -> List[Director]:
        return self._directors

    def add_review(self, review: Review):
        super().add_review(review)
        self._reviews.append(review)

    def get_reviews(self):
        return self._reviews


def populate(data_path: str, repo: MemoryRepository):

    reading_csv = MovieFileCSVReader(data_path)
    reading_csv.read_csv_file()

    for movie in reading_csv.dataset_of_movies:
        repo.add_movie(movie)




