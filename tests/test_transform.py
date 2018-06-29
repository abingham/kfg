from kfg.config import Config, ConfigValueError
import pytest


class CustomError(Exception):
    pass


class Transformer:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __call__(self, val):
        raise self.exc_type()


@pytest.fixture(scope='module',
                params=Config.DEFAULT_TRANSFORM_EXCEPTIONS)
def default_transform_exception(request):
    "Fixture yield each of the default transform exceptions."
    return request.param


def test_transform_violation_raises_ConfigValueError(
        config,
        key,
        default_transform_exception):
    config[key] = 'bar'
    config.set_transform(
        key=key,
        transform=Transformer(default_transform_exception),
    )
    with pytest.raises(ConfigValueError):
        config[key]


def test_transform_detects_custom_exception(config, key):
    config[key] = 'bar'

    config.set_transform(
        key=key,
        transform=Transformer(CustomError),
        exceptions=(CustomError,)
    )

    with pytest.raises(ConfigValueError):
        config[key]


def test_transform_ignores_exceptions_out_of_spec(
        config, key, default_transform_exception):

    config[key] = 'bar'

    config.set_transform(
        key=key,
        transform=Transformer(default_transform_exception),
        exceptions=(CustomError,)
    )

    with pytest.raises(default_transform_exception):
        config[key]
