from flask import Blueprint, request, render_template, redirect, url_for, session

import movies.adapters.repository as repo
import movies.utilities.services as services

# Configure Blueprint.
utilities_blueprint = Blueprint(
    'utilities_bp', __name__)


def get_genres_and_urls():
    genre_names = services.get_genre_names(repo.repo_instance)
    genre_urls = dict()
    for genre_name in genre_names:
        genre_urls[genre_name] = url_for('movies_bp.movies_by_genre', genre=genre_name)

    return genre_urls


def get_selected_movies(quantity=3):
    movies = services.get_random_movies(quantity, repo.repo_instance)

    return movies


def selected_movies_on_page(current_rank):
    movies = services.movies_on_page(current_rank, repo.repo_instance)

    return movies
