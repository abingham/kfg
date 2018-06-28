from kfg.config import Config
import pytest


@pytest.fixture
def config():
    "Fixture providing an empty Config."
    return Config()


@pytest.fixture(scope='module',
                params=[
                    'foo',
                    ('foo', 'bar'),
                    (1,),
                    ('a', 'qwerty', 3),
                    (1, 2, 3),
                ])
def key(request):
    "Fixture providing various valid keys."
    return request.param
