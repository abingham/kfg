from kfg.config import Config
import pytest


@pytest.fixture
def config():
    return Config()
