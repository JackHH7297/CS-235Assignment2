import pytest

from flask import session


def test_movies_without_rank(client):
    response = client.get('/movies_by_rank?rank=1')
    assert response.status_code == 200

    assert b'1. Guardians of the Galaxy (2014)' in response.data
    assert b'James Gunn' in response.data


def test_movies_with_rank(client):
    response = client.get('/movies_by_rank?rank=1000')
    assert response.status_code == 200

    assert b'1000. Nine Lives (2016)' in response.data
    assert b'Barry Sonnenfeld' in response.data


