import os
from flask import Flask

import movies.adapters.repository as repo
from movies.adapters.memory_repository import MemoryRepository, populate


def create_app(test_config=None):
    # Create the Flask app object.
    app = Flask(__name__)

    # Configure the app from configuration-file settings.
    app.config.from_object('config.Config')
    data_path = os.path.join('movies', 'adapters', 'data', 'Data1000Movies.csv')

    if test_config is not None:
        # Load test configuration, and overrride any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    # Build the application - these steps require an application context.
    with app.app_context():
        # Register blueprints.
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .movie import movie
        app.register_blueprint(movie.movies_blueprint)

        from .utilities import utilities
        app.register_blueprint(utilities.utilities_blueprint)

    return app
