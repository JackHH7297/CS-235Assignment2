import csv

from movies.domain.model import Movie, Actor, Genre, Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = []
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()
        self.__filtered_movies_by_genre = []
        self.__filtered_movies_by_director = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            index = 0
            for row in movie_file_reader:
                # Read in Title
                title = row['Title']

                # Read in Year
                release_year = int(row['Year'])
                movie = Movie(title, release_year)
                self.__dataset_of_movies.append(movie)

                # Read in description
                description = row["Description"]
                movie.description = description

                # Read in runtime
                runtime = row["Runtime (Minutes)"]
                movie.runtime_minutes = int(runtime)

                # Read in Actors
                actors = row['Actors']
                actor = actors.split(",")
                for i in actor:
                    actor = i.strip()
                    movie.add_actor(Actor(actor))
                    self.__dataset_of_actors.add(Actor(actor))

                # Read in Directors
                director = row['Director']
                movie.director = Director(director)
                self.__dataset_of_directors.add(Director(director))

                # Read in Genre
                genres = row['Genre']
                genre = genres.split(",")
                for i in genre:
                    a = i.strip()
                    movie.add_genre(Genre(a))
                    self.__dataset_of_genres.add(Genre(a))

                # Read in Rank
                rank = row["Rank"]
                movie.rank = rank

                # Read in Rating
                rating = row["Rating"]
                movie.rating = rating

                # Read in Votes
                vote = row["Votes"]
                movie.votes = vote

                # Read in revenue
                revenue = row["Revenue (Millions)"]
                movie.revenue = revenue

                # Read in meta_scores
                metascore = row["Metascore"]
                movie.metascore = metascore

                index += 1

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    # Returns movies with specific Genre(s)
    @property
    def movies_filtered_by_genre(self):
        return self.__filtered_movies_by_genre

    # Returns movies with a specific Director
    @property
    def movies_filtered_by_director(self):
        return self.__filtered_movies_by_director

    # Retrieve the Movie object of a movie
    def movie_object(self, name):
        for movies in self.__dataset_of_movies:
            if name == movies.title:
                return movies

    def filter_by_genre(self, genre):
        if type(genre) == Genre:
            for movie in self.__dataset_of_movies:
                if genre in movie.genres:
                    self.__filtered_movies_by_genre.append(movie)
        elif type(genre) == list:
            for element in genre:
                if type(element) == Genre:
                    continue
                else:
                    return
            for movie in self.__dataset_of_movies:
                lista = [i for i in movie.genres if i in genre]
                listb = [i for i in genre if i in movie.genres]
                if lista == listb == genre:
                    self.__filtered_movies_by_genre.append(movie)

    def filter_by_director(self, director):
        if type(director) == Director:
            for movie in self.__dataset_of_movies:
                if movie.director == director:
                    self.__filtered_movies_by_director.append(movie)

