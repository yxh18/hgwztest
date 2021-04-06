import pytest


@pytest.fixture(scope='function')
def user():
    return '123'
