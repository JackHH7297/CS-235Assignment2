from movies.domain.model import Movie, Director, Genre, Actor, User, Review


def test_title_normal():
    movie = Movie("Spirited Away", 1995)

    assert movie.title == "Spirited Away"
    assert movie.release_year == 1995


def test_title_year_less_than_1900():
    movie = Movie("Spirited Away", 1885)

    assert movie.title == "Spirited Away"
    assert movie.release_year == None


def test_title_year_eq_1900():
    movie = Movie("Spirited Away", 1990)

    assert movie.title == "Spirited Away"
    assert movie.release_year == 1990


def test_title__year_non_integer():
    movie = Movie("Spirited Away", "1885")

    assert movie.title == "Spirited Away"
    assert movie.release_year == None


def test_non_string_title_year_non_integer():
    movie = Movie(12345, "1885")

    assert movie.title == None
    assert movie.release_year == None


def test_non_string_title_year():
    movie = Movie(12345, 1990)

    assert movie.title == None
    assert movie.release_year == 1990


def test_none_none():
    movie = Movie(None, None)

    assert movie.title == None
    assert movie.release_year == None


def test_empty_normal():
    movie = Movie("", 1899)

    assert movie.title == None
    assert movie.release_year == None


def test_eq_same_name_diff_year():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Spirited Away", 2005)
    equal = movie1 == movie2
    eq = movie1 == movie2
    assert eq == False
    assert equal == False


def test_eq_same_name_same_year():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Spirited Away", 2000)
    equal = movie1 == movie2
    eq = movie1 == movie2
    assert eq == True
    assert equal == True


def test_eq_diff_name_same_year():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Spirited", 2000)
    equal = movie1 == movie2
    eq = movie1 == movie2
    assert eq == False
    assert equal == False


def test_eq_diff_name_diff_year():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Spirited", 2005)
    equal = movie1 == movie2
    eq = movie1 == movie2
    assert eq == False
    assert equal == False


def test_lt_same_name_same_year():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Spirited Away", 2000)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == True
    assert lt == False


def test_lt_same_name_diff_year():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Spirited Away", 2005)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == True


def test_lt_diff_name_same_year():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Spirited", 2000)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == False


def test_lt_diff_name_diff_year():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Spirited", 2008)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == False


def test_lt_diff_name_none_year_1():
    movie1 = Movie("Spirited Away", 1550)
    movie2 = Movie("Spirited", 2008)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == False


def test_lt_diff_name_none_year_2():
    movie1 = Movie("Spirited Away", 2008)
    movie2 = Movie("Spirited", 1750)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == False


def test_lt_same_name_none_year_1():
    movie1 = Movie("Spirited Away", 1550)
    movie2 = Movie("Spirited Away", 2008)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == True


def test_lt_same_name_none_year_2():
    movie1 = Movie("Spirited Away", 2008)
    movie2 = Movie("Spirited Away", 1446)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == False


def test_lt_none_name1_same_year():
    movie1 = Movie(None, 2008)
    movie2 = Movie("Spirited Away", 2008)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == True


def test_lt_none_name2_same_year():
    movie1 = Movie("Spirited Away", 2008)
    movie2 = Movie(None, 2008)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == False


def test_lt_same_name_none_year1():
    movie1 = Movie("Spirited Away", None)
    movie2 = Movie("Spirited Away", 2008)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == True



def test_lt_same_name_none_year2():
    movie1 = Movie("Spirited Away", 2008)
    movie2 = Movie("Spirited Away", None)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == False
    assert lt == False


def test_lt_same_name_none_year_both():
    movie1 = Movie("Spirited Away", None)
    movie2 = Movie("Spirited Away", None)
    lt = movie1 < movie2
    eq = movie1 == movie2
    assert eq == True
    assert lt == False


def test_hash_1():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Spirited Away", 2000)
    movie3 = Movie("Spirited Away", 2001)
    movie4 = Movie("Spirited Away", 2002)
    movie5 = Movie("Spirited Away", 2003)
    movie6 = Movie("Spirited Away", 2004)
    movie7 = Movie("Spirited Away", 1885)

    seta = {movie1, movie2, movie3, movie4, movie5, movie6, movie7}
    assert seta == {movie1, movie3, movie4, movie5, movie6, movie7}


def test_change_title():
    movie1 = Movie("Spirited Awa", 2000)
    movie2 = Movie("Your Nam", 2000)
    movie3 = Movie("Batma", 2000)

    movie1.title = "                         Spirited Away              "
    movie2.title = "          Your     Name          "
    movie3.title = "         Batman     "

    assert movie1.title == "Spirited Away"
    assert movie2.title == "Your     Name"
    assert movie3.title == "Batman"


def test_change_description():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Your Name", 2000)
    movie3 = Movie("Batman", 2000)
    movie4 = Movie(None, None)

    movie1.description = "Best movie"
    movie2.description = ""
    movie3.description = 123124124
    movie4.description = None

    assert movie1.description == "Best movie"
    assert movie2.description == ""
    assert movie3.description == ""
    assert movie4.description == ""


def test_director():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Your Name", 2000)
    movie3 = Movie("Batman", 2000)
    movie4 = Movie(None, None)

    movie1.director = Director("BB Huang")
    assert movie1.director == Director("BB Huang")
    movie1.director = Director("Jack Huang")
    assert movie1.director == Director("Jack Huang")
    movie2.director = "Jack Huang"
    assert movie2.director == None
    movie3.director = 123456
    assert movie3.director == None
    movie3.director = None
    assert movie4.director == None


def test_actors():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Your Name", 2000)
    movie3 = Movie("Batman", 2000)
    movie4 = Movie(None, None)

    movie1.actors = [Actor("Jack Huang"), Actor("James Huang"), Actor("Ron Huang"), Actor("Jane Tang")]
    assert movie1.actors == [Actor("Jack Huang"), Actor("James Huang"), Actor("Ron Huang"), Actor("Jane Tang")]
    movie2.actors = [Actor("Jack Huang"), "James Huang", Actor("Ron Huang"), 123456]
    assert movie2.actors == []
    movie3.actors = Actor("Jack Huang")
    assert movie3.actors == [Actor("Jack Huang")]
    movie4.actors = "Jack Huang"
    assert movie4.actors == []


def test_genres():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Your Name", 2000)
    movie3 = Movie("Batman", 2000)
    movie4 = Movie(None, None)

    movie1.genres = [Genre("Comedy"), Genre("Horror"), Genre("Sci-fi")]
    assert movie1.genres == [Genre("Comedy"), Genre("Horror"), Genre("Sci-fi")]
    movie2.genres = [Genre("Comedy"), Genre("Horror"), Genre("Sci-fi"), 12345]
    assert movie2.genres == []
    movie3.genres = Genre("Comedy")
    assert movie3.genres == [Genre("Comedy")]
    movie4.genres = "Comedy"
    assert movie4.genres == []


def test_runtime():
    movie1 = Movie("Spirited Away", 2000)
    movie2 = Movie("Your Name", 2000)
    movie3 = Movie("Batman", 2000)
    movie4 = Movie(None, None)

    movie1.runtime_minutes = 150
    assert movie1.runtime_minutes == 150
    movie2.runtime_minutes = 1
    assert movie2.runtime_minutes == 1
    movie3.runtime_minutes = "150"
    assert movie3.runtime_minutes == 0
    movie4.runtime_minutes = None
    assert movie4.runtime_minutes == 0


def test_add_actor():
    movie1 = Movie("Spirited Away", 2000)

    movie1.actors = [Actor("James Huang")]
    movie1.add_actor(Actor("Jack Huang"))
    assert movie1.actors == [Actor("James Huang"), Actor("Jack Huang")]
    movie1.add_actor("Ron Huang")
    movie1.add_actor("")
    movie1.add_actor(None)
    movie1.add_actor(21345648)
    assert movie1.actors == [Actor("James Huang"), Actor("Jack Huang")]


def test_remove_actor():
    movie1 = Movie("Spirited Away", 2000)

    movie1.actors = [Actor("James Huang"), Actor("Ron Huang")]
    movie1.add_actor(Actor("Jack Huang"))
    movie1.remove_actor(Actor("Jack Huang"))
    assert movie1.actors == [Actor("James Huang"), Actor("Ron Huang")]
    movie1.remove_actor(Actor("James Huang"))
    movie1.remove_actor(Actor("Jawer"))
    movie1.remove_actor(Actor("Jackwerang"))
    movie1.remove_actor(Actor("Jweruang"))
    assert movie1.actors == [Actor("Ron Huang")]
    movie1.remove_actor(Actor("Ron Huang"))
    assert movie1.actors == []


def test_add_genre():
    movie1 = Movie("Spirited Away", 2000)

    movie1.genres = [Genre("Comedy")]
    movie1.add_genre(Genre("Horror"))
    assert movie1.genres == [Genre("Comedy"), Genre("Horror")]
    movie1.add_genre("Scifi")
    movie1.add_genre(Genre("Hhiya"))
    movie1.add_genre("")
    movie1.add_genre(None)
    movie1.add_genre(21345648)
    assert movie1.genres == [Genre("Comedy"), Genre("Horror"), Genre("Hhiya")]


def remove_genre():
    movie1 = Movie("Spirited Away", 2000)

    movie1.genres = [Genre("Comedy")]
    movie1.add_genre(Genre("Horror"))
    movie1.add_genre(Genre("Happy ending"))
    assert movie1.genres == [Genre("Comedy"), Genre("Horror"), Genre("Happy ending")]
    movie1.remove_genre("Scifi")
    movie1.remove_genre(Genre("Hhiya"))
    movie1.remove_genre("")
    movie1.remove_genre(None)
    movie1.remove_genre(21345648)
    movie1.remove_genre(Genre("Happy ending"))
    assert movie1.genres == [Genre("Comedy"), Genre("Horror")]
    movie1.remove_genre(Genre("Comedy"))
    assert movie1.genres == [ Genre("Horror")]
    movie1.remove_genre(Genre("Horror"))
    assert movie1.genres == []


def test_code_runner():
    movie = Movie("Moana", 2016)
    assert movie.title == "Moana"
    assert movie.release_year == 2016
    director = Director("Ron Clements")
    movie.director = director
    assert movie.director == Director("Ron Clements")

    actors = [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]
    for actor in actors:
        movie.add_actor(actor)
    assert movie.actors == [Actor("Auli'i Cravalho"), Actor("Dwayne Johnson"), Actor("Rachel House"), Actor("Temuera Morrison")]

    movie.runtime_minutes = 107
    assert movie.runtime_minutes == 107


def test_user_password_normal():
    user = User("    Jack Huang     ", "gOod one")

    assert user.user_name == "jack huang"
    assert user.password == "gOod one"


def test_user_password_non_string():
    user = User(1234124, 123124)

    assert user.user_name is None
    assert user.password is None


def test_user_password_string_int():
    user = User("Jack Huang", "123124")

    assert user.user_name == "jack huang"
    assert user.password == "123124"


def test_empty_watched_movies_and_reviews():
    user = User("Jack Huang", "123124")

    assert user.watched_movies == []
    assert user.reviews == []


def test_add_movies_and_length():
    user = User("Jack Huang", "123124")
    movie1 = Movie("Your Name", 2000)
    movie2 = Movie("Spirited Away", 1995)
    movie3 = Movie("Avengers 4", 1899)
    movie1.runtime_minutes = 100
    movie2.runtime_minutes = 150
    movie3.runtime_minutes = 300

    assert user.watched_movies == []
    user.watch_movie(movie1)
    user.watch_movie(movie2)
    user.watch_movie(movie3)
    assert user.watched_movies == [Movie("Your Name", 2000), Movie("Spirited Away", 1995), Movie("Avengers 4", None)]
    assert user.time_spent_watching_movies_minutes == 550


def test_add_review():
    user = User("Jack Huang", "123124")
    movie1 = Movie("Your Name", 2000)
    movie2 = Movie("Spirited Away", 1995)
    movie3 = Movie("Avengers 4", 1899)

    review1 = Review(user, movie1, "Good 1", 1)
    review2 = Review(user, movie2, "Good 2", 2)
    review3 = Review(user, movie3, "Good 3", 3)

    assert user.reviews == []
    user.add_review(review1)
    user.add_review(review2)
    user.add_review(review3)
    assert user.reviews == [Review(user, movie1, "Good 1", 1), Review(user, movie2, "Good 2", 2),
                            Review(user, movie3, "Good 3", 3)]


def test_eq_same_name():
    user1 = User("qwer", 12345)
    user2 = User("qwer", "qwer")

    eq = user1 == user2
    assert eq == True


def test_eq_same_name_caps_space():
    user1 = User(" QweR      ", 12345)
    user2 = User("     qWEr ", "qwer")

    eq = user1 == user2
    assert eq == True


def test_eq_diff_name():
    user1 = User(" Q weR      ", 12345)
    user2 = User("     qWEr ", "qwer")

    eq = user1 == user2
    assert eq == False


def test_lt_same_name():
    user1 = User(" QweR      ", "aaaaa")
    user2 = User("     qWEr ", "A")

    lt = user1 < user2
    assert lt == False


def test_lt_diff_name():
    user1 = User("Hi", 12345)
    user2 = User("HI", "qwer")

    lt = user1 < user2
    assert lt == False


def test_lt_none_name():
    user1 = User(None, 12345)
    user2 = User("HI", "qwer")

    lt = user1 < user2
    assert lt == True


def test_hash_():
    user1 = User("None", "qwer")
    user2 = User("HI", "qwer")
    user3 = User("Jack", "qwer")
    user4 = User("  jack      ", "qwer")

    seta = {user1, user2, user3, user4}
    assert seta == {User("None", "qwer"), User("HI", "qwer"), User("Jack", "qwer"), User("  jack      ", "qwer")}