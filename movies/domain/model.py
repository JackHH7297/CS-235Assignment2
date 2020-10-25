from datetime import datetime
from random import Random, random


class Director:

    def __init__(self, director_full_name: str):
        if director_full_name == "" or type(director_full_name) is not str:
            self.__director_full_name = None
        else:
            self.__director_full_name = director_full_name.strip()

    @property
    def director_full_name(self) -> str:
        return self.__director_full_name

    def __repr__(self):
        return f"<Director {self.__director_full_name}>"

    def __eq__(self, other):
        if self.__director_full_name == other.__director_full_name:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.__director_full_name < other.__director_full_name

    def __hash__(self):
        return hash(self.__director_full_name)


class Actor:

    def __init__(self, name):
        if name != "" and isinstance(name, str):
            self.actor_full_name = name
        else:
            self.actor_full_name = None

        self.actor_colleague = []

    def __repr__(self):
        return "<Actor {}>".format(self.actor_full_name)

    def __eq__(self, other):
        return self.actor_full_name == other.actor_full_name

    def __lt__(self, other):
        return self.actor_full_name < other.actor_full_name

    def __hash__(self):
        return hash(self.actor_full_name)

    @property
    def actor_name(self):
        return self.actor_full_name

    def add_actor_colleague(self, colleague):
        self.actor_colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        if colleague in self.actor_colleague:
            return True
        return False


class Movie:

    def __init__(self, title = None, year = None):
        if title == None:
            self.__title = None
        elif title != None and type(title) == str and title != "":
            self.__title = title.strip()
        else:
            self.__title = None

        if year == None:
            self.__release_year = None
        elif year != None and type(year) == int and year >= 1900:
            self.__release_year = year
        else:
            self.__release_year = None

        self.__director = None
        self.__description = ""
        self.__runtime_minutes = 0
        self.__actor_list = []
        self.__genres_list = []

        # Extension
        self.__rank = None
        self.__rating = None
        self.__revenue = None
        self.__metascore = None
        self.__votes = None

        self.__review = []

    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank):
        try:
            rank = int(rank)
            if type(rank) == int:
                if rank > 0:
                    self.__rank = rank
        except ValueError:
            pass

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, rating):
        try:
            rating = float(rating)
            if 1 <= rating <= 10:
                self.__rating = rating
        except ValueError:
            pass

    @property
    def revenue(self):
        return self.__revenue

    @revenue.setter
    def revenue(self, revenue):
        try:
            revenue = float(revenue.strip())
            self.__revenue = revenue
        except ValueError:
            pass

    @property
    def metascore(self):
        return self.__metascore

    @metascore.setter
    def metascore(self, score):
        try:
            score = int(score.strip())
            if 0 <= score <= 100:
                self.__metascore = score
        except ValueError:
            pass

    @property
    def votes(self):
        return self.__votes

    @votes.setter
    def votes(self, vote):
        try:
            vote = int(vote)
            if vote >= 0:
                self.__votes = vote
        except ValueError:
            pass

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, movie_name):
        if isinstance(movie_name, str) and movie_name != "":
            self.__title = movie_name.strip()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, descript):
        if isinstance(descript, str) and descript != "":
            self.__description = descript.strip()

    @property
    def actors(self):
        return self.__actor_list

    @actors.setter
    def actors(self, list_of_actors):
        if type(list_of_actors) == list:
            for i in list_of_actors:
                if type(i) != Actor:
                    return
            self.__actor_list = list_of_actors
        else:
            if type(list_of_actors) == Actor:
                self.__actor_list.append(list_of_actors)

    @property
    def genres(self):
        return self.__genres_list

    @genres.setter
    def genres(self, list_of_genres):
        if type(list_of_genres) == list:
            for i in list_of_genres:
                if type(i) != Genre:
                    return
            self.__genres_list = list_of_genres
        else:
            if type(list_of_genres) == Genre:
                self.__genres_list.append(list_of_genres)

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, a_director):
        if type(a_director) == Director:
            self.__director = a_director

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, value):
        if type(value) == int:
            if value <= 0:
                raise ValueError
            else:
                self.__runtime_minutes = value

    def __lt__(self, other):
        if self.__title == None or other.__title == None:
            if other.__title != None:
                return True
            else:
                if self.__release_year == None and other.__release_year == None:
                    return False
                elif self.__release_year != None:
                    if other.__release_year != None:
                        if self.__release_year < other.__release_year:
                            return True
                        else:
                            return False
                    else:
                        return False

        elif self.__title < other.__title:
            return True

        elif self.__title == other.__title:
            if self.__release_year == None and other.__release_year == None:
                return False
            elif self.__release_year != None:
                if other.__release_year != None:
                    if self.__release_year < other.__release_year:
                        return True
                else:
                    return False
            elif self.__release_year == None:
                if other.__release_year != None:
                    return True

        return False

    def __hash__(self):
        unique_name = self.__title + str(self.__release_year)
        return hash(unique_name)

    def __repr__(self):
        return "<Movie {}, {}>".format(self.__title, self.__release_year)

    def __eq__(self, other):
        if self.__title == other.__title:
            if self.__release_year == other.__release_year:
                return True
        return False

    def add_actor(self, add_actor):
        if type(add_actor) == Actor:
            self.__actor_list.append(add_actor)

    def remove_actor(self, remove_actor):
        if remove_actor in self.__actor_list:
            self.__actor_list.remove(remove_actor)

    def add_genre(self, add_genre):
        if type(add_genre) == Genre:
            self.__genres_list.append(add_genre)

    def remove_genre(self, remove_genre):
        if remove_genre in self.__genres_list:
            self.__genres_list.remove(remove_genre)

    def has_actor(self, actor: str):
        if type(actor) != str:
            return False
        actor1 = Actor(actor)
        return actor1 in self.__actor_list

    @property
    def release_year(self):
        return self.__release_year

    def add_review(self, review):
        self.__review.append(review)

    def is_tagged(self):
        return len(self.__genres_list) > 0

    def is_tagged_by(self, genre):
        return genre in self.__genres_list


class Genre:
    def __init__(self, genre):

        if genre != "":
            self._genre_name = genre

        else:
            self._genre_name = None
        self._tagged_movies = []

    def __repr__(self):
        return "<Genre {}>".format(self.genre_name)

    def __eq__(self, other):
        return self.genre_name == other.genre_name

    def __lt__(self, other):
        return self.genre_name < other.genre_name

    def __hash__(self):
        return hash(self.genre_name)

    @property
    def number_of_tagged_movies(self) -> int:
        return len(self.tagged_movies)

    @property
    def genre_name(self):
        return self._genre_name

    @property
    def tagged_movies(self):
        return self._tagged_movies

    def is_applied_to(self, movie: Movie) -> bool:
        return movie in self._tagged_movies

    def add_movie(self, movie: Movie):
        self._tagged_movies.append(movie)


class Review:

    def __init__(self, user, movie, review_text, rating):
        self.__user = user
        if type(movie) == Movie:
            self.__movie = movie
        else:
            self.__movie = None

        if type(review_text) == str:
            self.__review_text = review_text
        else:
            self.__review_text = ""

        if 0 < rating < 11:
            self.__rating = rating
        else:
            self.__rating = None

        self.__timestamp = datetime.today()

    def __repr__(self):
        return "{} \nReview: {}\nRating: {}\nDate: {}".\
            format(self.__movie, self.__review_text, self.__rating, self.__timestamp)

    def __eq__(self, other):
        if self.__movie == other.__movie:
            if self.__review_text == other.__review_text:
                if self.__rating == other.__rating:
                    if self.__timestamp == other.__timestamp:
                        return True
        return False

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return self.__review_text

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def user(self):
        return self.__user


class User:

    def __init__(self, username, password):
        if type(username) == str:
            self.__user_name = username.strip().lower()
        else:
            self.__user_name = None

        if type(password) == str:
            self.__password = password
        else:
            self.__password = None

        self.__watched_movies = []
        self.__reviews = []
        self.__time_spent_watching_movies_minutes = 0

    def __repr__(self):
        return "<User {}>".format(self.__user_name)

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        if self.__user_name is None:
            if other.__user_name is None:
                return False
            else:
                return True
        else:
            if other.__user_name is None:
                return False
            else:
                return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if type(movie) == Movie:
            self.__watched_movies.append(movie)
            self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if type(review) == Review:
            self.__reviews.append(review)

    @property
    def user_name(self):
        return self.__user_name

    @property
    def password(self):
        return self.__password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @property
    def reviews(self):
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent_watching_movies_minutes


class WatchList:

    def __init__(self):
        self.__watchlist = []

    def add_movie(self, movie):
        if type(movie) == Movie:
            if movie not in self.__watchlist:
                self.__watchlist.append(movie)

    def remove_movie(self, movie):
        if type(movie) == Movie:
            if movie in self.__watchlist:
                self.__watchlist.remove(movie)

    def select_movie_to_watch(self, index):
        if index < len(self.__watchlist):
            return self.__watchlist[index]
        return None

    def size(self):
        return len(self.__watchlist)

    def first_movie_in_watchlist(self):
        if len(self.__watchlist) > 0:
            return self.__watchlist[0]

        return None

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__watchlist):
            movie = self.__watchlist[self.n]
            self.n += 1
            return movie
        else:
            raise StopIteration

    # Extra methods: add a random movie to watchlist
    def add_random(self, movie_list, seed=None):
        random_movie = None

        if seed is None:
            loop = True
            while loop:
                random_movie = random.choice(movie_list)
                if random_movie not in self.__watchlist:
                    self.__watchlist.append(random_movie)
                    break
        else:
            ran = Random(seed)
            loop = True
            while loop:
                random_movie = movie_list[ran.randint(0, len(movie_list) - 1)]
                if random_movie not in self.__watchlist:
                    self.__watchlist.append(random_movie)
                    break

        return random_movie


class ModelException(Exception):
    pass


def make_review(user, movie, rating_text, rating):
    review = Review(user, movie, rating_text, rating)
    user.add_review(review)
    movie.add_review(review)


def make_genre_association(movie: Movie, genre: Genre):
    if genre.is_applied_to(movie):
        raise ModelException(f'Genre {genre.genre_name} already applied to Movie "{movie.title}"')

    movie.add_genre(genre)
    genre.add_movie(movie)

