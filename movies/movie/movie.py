from flask import Blueprint
from flask import request, render_template, redirect, url_for, session


import movies.adapters.repository as repo
import movies.utilities.utilities as utilities
import movies.movie.services as services

# Configure Blueprint.
movies_blueprint = Blueprint(
    'movies_bp', __name__)


@movies_blueprint.route('/movies_by_rank', methods=['GET'])
def movie_by_rank():
    # Read query parameters.
    target_rank = request.args.get('rank')

    # Fetch the first and last movies in the series.
    first_movie = services.get_first_movie(repo.repo_instance)
    last_movie = services.get_last_movie(repo.repo_instance)

    if target_rank is None:
        # No date query parameter, so return movies starting from rank 1 of the series.
        target_rank = first_movie['rank']
    else:
        target_rank = int(target_rank)

    movie, previous_rank, next_rank = services.get_movie_by_a_rank(target_rank, repo.repo_instance)

    movies_to_display = services.mov_on_page(target_rank, repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if movie is not None:
        # There is a movie with the given rank
        if previous_rank is not None:
            # There is a movie with -1 smaller rank. So generate URLs for the 'previous' and 'first' navigation buttons.
            prev_movie_url = url_for('movies_bp.movie_by_rank', rank=previous_rank)
            first_movie_url = url_for('movies_bp.movie_by_rank', rank=first_movie['rank'])
        if next_rank is not None:
            # There are movies with +1 larger rank, so generate URLs for the 'next' and 'last' navigation buttons.
            next_movie_url = url_for('movies_bp.movie_by_rank', rank=next_rank)
            last_movie_url = url_for('movies_bp.movie_by_rank', rank=last_movie['rank'])

        # Generate the webpage to display the articles.
        return render_template(
            'movies/movies.html',
            title='Movies',
            movie_title=target_rank,
            movies=movie,
            selected_movies=utilities.get_selected_movies(8),
            selected_movies_on_page=movies_to_display,
            genre_urls=utilities.get_genres_and_urls(),
            first_movie_url=first_movie_url,
            last_movie_url=last_movie_url,
            prev_movie_url=prev_movie_url,
            next_movie_url=next_movie_url,
        )
    # No articles to show, so return the homepage.
    return redirect(url_for('home_bp.home'))


@movies_blueprint.route('/movies_by_genre', methods=['GET'])
def movies_by_genre():
    movies_per_page = 3

    # Read query parameters.
    genre_name = request.args.get('genre')
    cursor = request.args.get('cursor')

    if cursor is None:
        # No cursor query parameter, so initialise cursor to start at the beginning.
        cursor = 0
    else:
        # Convert cursor from string to int.
        cursor = int(cursor)

    # Retrieve movie ranks for movies has the genre of genre_name.
    movie_ranks = services.get_movies_ranks_for_genre(genre_name, repo.repo_instance)

    movies = services.get_movies_by_rank(movie_ranks[cursor:cursor + movies_per_page], repo.repo_instance)

    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if cursor > 0:
        # There are preceding movies, so generate URLs for the 'previous' and 'first' navigation buttons.
        prev_movie_url = url_for('movies_bp.movies_by_genre', genre=genre_name, cursor=cursor - movies_per_page)
        first_movie_url = url_for('movies_bp.movies_by_genre', genre=genre_name)

    if cursor + movies_per_page < len(movie_ranks):
        # There are further movies, so generate URLs for the 'next' and 'last' navigation buttons.
        next_movie_url = url_for('movies_bp.movies_by_genre', genre=genre_name, cursor=cursor + movies_per_page)

        last_cursor = movies_per_page * int(len(movie_ranks) / movies_per_page)
        if len(movie_ranks) % movies_per_page == 0:
            last_cursor -= movies_per_page
        last_movie_url = url_for('movies_bp.movies_by_genre', genre=genre_name, cursor=last_cursor)

    # Generate the webpage to display the movies.
    return render_template(
        'movies/movies.html',
        title='Movies',
        movies_title='Movies with genre ' + genre_name,
        movies=movies,
        selected_movies=utilities.get_selected_movies(len(movies) * 2),
        genre_urls=utilities.get_genres_and_urls(),
        first_movie_url=first_movie_url,
        last_movie_url=last_movie_url,
        prev_movie_url=prev_movie_url,
        next_movie_url=next_movie_url,
    )